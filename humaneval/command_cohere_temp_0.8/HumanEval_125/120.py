```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) ^ 1, txt.lower())))
    return words
```

The problem prompts us to return the number of lowercase letters with odd order in the alphabet if the string contains no whitespace or commas. This is achieved through the filter method, which filters falsey characters (characters that don't have the parity of their ASCII ordinal equal to one). The length of this filtered list is returned as the solution. If the string contains whitespace, we split it into a list of words by characterizing the string, and if it contains no whitespace we split the words by commas.