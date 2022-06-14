# CSV Normalizer

So, I originally went with a solution based on Python 3's CSV reader, and kept going deeper down the rabbit hole of UTF-8 edge cases and reading from stdin...when I remembered Pandas existed!  I quickly did a crash course on its CSV implementation and used it for most of the heavy lifting.  

After 4 hours this is what I haven't completed:
* Removing the 0 milliseconds from the seconds counter.  They all appear as XYZ.0
* Was not able to print when an error row was encountered and send that to stderr.  Pandas caught the errors and suppressed them.

## SETUP

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## RUN

```sh
python3 normalizer.py < input.csv > output.csv
```

## LINTING

```sh
flake8 normalizer.py 
black --check normalizer.py
isort --check normalizer.py
```