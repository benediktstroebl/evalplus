```python
def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != [''] else len(set(txt.lower())) % 2 == 1
```

The problem prompts the function `split_words` to return a list of words split on whitespace. However, if there is no whitespace in the string, it should split on commas instead. If the string has no commas or whitespace, it should return the number of lowercase letters with odd alphabetical order. The provided solution uses string manipulation and `split` functions to achieve the appropriate outcome based on the string contents.