```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) ^ 1, txt.lower())))
    return words
```

The code uses a conditional structure in order to choose the appropriate splitting mechanism depending on the contents of the string. If the string contains commas, it uses the `split` method to split the string into words, whereas if the string contains spaces, it also uses the `split` method to split the string into words. If neither commas nor spaces are present, it counts the number of letters that have an odd parity when interpreted as integers (which is to say, it counts the number of lowercase letters that come up "odd" in a numerical sense when converted to ASCII). This number is then returned as the list of words. The approach utilizes the fact that Python's `filter` streamlines counting when a list of boolean values is not needed.