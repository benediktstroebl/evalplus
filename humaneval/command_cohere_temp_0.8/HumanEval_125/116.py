```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([c for c in txt if c.islower() and ord(c) % 2 == 0])
    return words
```

The code solves the problem by performing the following steps:
1. Checks if the string `txt` contains a comma `,'` if it does, then it splits the string into a list of words using the split `,''` method, this way the list `[ 'Hello', 'world!' ]` is returned.
2. If the above condition is not met, it checks if the string contains whitespace `' '`, if it does, it splits the string into a list using the split method, this way the list `[ 'Hello', 'world!' ]` is returned.
3. If none of the above conditions are met, it counts the number of lowercase letters with an even index and returns the count, which corresponds to the given example `[ 'abcdef' ] == 3`. 
Therefore, 3 is returned as the list cannot be split using whitespace or commas. G