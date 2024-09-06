```python
import re

def split_words(txt):
    if re.search(r'\s', txt):
        return txt.split()
    elif re.search(r',', txt):
        return txt.split(',')
    else:
        return len(list(filter(lambda c: ord(c) > 14 and ord(c) % 2 == 0, txt.lower())))
```

The Python script uses regular expressions via the `re` module to efficiently determine the logic for word splitting. If whitespaces are detected using `re.search(r'\s', txt)`, the function splits the input text using the `split()` method, which splits on whitespace by default. If no whitespaces are found but commas are present, the text is split using `split(',')`. If neither whitespaces nor commas are present, the function returns the count of lowercase letters with odd ordinal values, filtered from the input text. This approach ensures a concise and effective solution.