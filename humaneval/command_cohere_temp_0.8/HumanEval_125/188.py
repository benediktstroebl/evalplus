```python
def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split(' ')
    return words if words != ',' else len(txt) if txt.islower() else None
```

The problem prompts the function `split_words` to return a list of words split on whitespace. However, if there is no whitespace in the string, it should split on commas instead. If neither whitespace nor commas exist in the string, the function should return the number of lowercase letters with an odd number of characters. The function uses Python's string methods `find` and `islower` to achieve these goals.