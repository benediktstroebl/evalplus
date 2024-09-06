```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([c for c in txt if c.islower() and ord(c) % 2 == 0])
    return words
```

The problem asks to return the list of words split on whitespace, if no whitespace exists in the text, it should split on commas. In the event of both commas and whitespace not being present in the text, we are asked to return the count of lowercase letters with an even alphabetical order. To achieve this, we utilize Python's string split methods to split on commas or whitespace, and in the absence of both, we use a list comprehension to find odd lowercase letters and their count.