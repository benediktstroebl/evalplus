```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([c for c in txt if c.islower() and ord(c) % 2 == 0])
    return words
```

The problem prompts us to return the number of lowercase letters with an even order in the alphabet if the string doesn't contain whitespaces or commas, which can be achieved using Python's list and filter functionalities as follows: `[c for c in txt if c.islower() and ord(c) % 2 == 0]`. The `islower()` method returns `True` if the character is lowercase and `False` otherwise, `ord()` gives the corresponding ASCII value of a character, and the modulus operator `%` returns the remainder of division by 2, which will be `0` if the ASCII value is even. Combining these concepts we return the requested value.