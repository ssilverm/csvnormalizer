import datetime
import sys

import pandas as pd
import pytz


def format_eastern(pacific_time):
    # https://medium.com/easyread/understanding-about-rfc-3339-for-datetime-formatting-in-software-engineering-940aa5d5f68a
    # https://stackoverflow.com/questions/8556398/generate-rfc-3339-timestamp-in-python

    pacific = datetime.datetime.strptime(pacific_time, "%m/%d/%y %I:%M:%S %p")

    et = pytz.timezone("America/New_York")
    pt = pytz.timezone("America/Los_Angeles")

    now_pt = pt.normalize(pt.localize(pacific))
    now_et = et.normalize(now_pt.astimezone(et))

    return now_et.isoformat()


def format_zip(zip_code):
    # https://stackoverflow.com/questions/66236790/is-there-a-way-to-format-a-zip-code-in-pandas-using-leading-00s
    return zip_code.zfill(5)


def format_seconds(duration):
    # This feels like a hack...
    duration = duration.split(":")
    delta = datetime.timedelta(
        hours=int(duration[0]),
        minutes=int(duration[1]),
        seconds=int(float(duration[2])),
    )
    seconds = pd.Timedelta(delta).total_seconds()
    return seconds


with open(0, "r", errors="replace") as f:
    df = pd.read_csv(
        f,
        converters={
            "Timestamp": format_eastern,
            "ZIP": format_zip,
            "FullName": lambda x: x.upper(),
            "FooDuration": format_seconds,
            "BarDuration": format_seconds,
        },
    )

# Double check this isn't off by one row...
df["TotalDuration"] = df["FooDuration"] + df["BarDuration"]

df.to_csv(sys.stdout, index=False)
