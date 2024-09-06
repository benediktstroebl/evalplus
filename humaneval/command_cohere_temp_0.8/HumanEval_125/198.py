```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) % 2, txt.lower())))
    return words
```

The problem prompts us to return the number of lowercase letters with odd order in the alphabet if the string contains neither whitespace nor comma. To achieve this, we filter the lowercase letters of the string and calculate their parity using the `% 2` modulo operation, which returns an odd value for every character with odd order in the alphabet. Finally, we use `list()` to force filtering to return a list, and `len()` to get the desired number of characters.