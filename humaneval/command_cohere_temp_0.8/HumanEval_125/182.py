```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([c for c in txt if c.islower() and ord(c) % 2 == 0])
    return words
```

The problem prompts us to return the number of lower-case letters with odd order in the alphabet if the string contains no whitespace or commas. To achieve this, we utilize Python's list comprehension capability to find the count of lowercase letters with an even alphabet order, then negate the result to indicate the desired count of odd-ordered letters.