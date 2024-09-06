```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([c for c in txt if c.islower() and ord(c) % 2 == 0])
    return words
```

The problem prompts us to return the number of lowercase letters with an even order in the alphabet if no whitespace or comma exists in the string. For example, 'abcde' returns 5 because 'a', 'b', 'd', and 'e' have an even order in the alphabet whereas 'c' does not. The function will first check for whitespace, then check for commas, and finally use a list comprehension to find the number of letters with an even order in the alphabet.