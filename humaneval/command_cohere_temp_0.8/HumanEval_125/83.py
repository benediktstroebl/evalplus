```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) ^ 1, txt.lower())))
    return words
```

The problem prompts us to return the number of lowercase letters with odd order in the alphabet if the string contains no whitespace or commas. This is achieved using the filter and lambda functions to return a list of indices of letters with odd ordinal values, and then obtaining the length of this list. The lambda function filters out all characters that have odd parity when converted to an integer using the function `ord()`.