```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The function `is_happy()` checks if the input string `s` is happy by following the problem's description. It first checks if the string's length is at least 3 using the `len(s) < 3` condition. If the length is less than 3, it returns `False` since a happy string must have at least three letters.

Then, we calculate the uniqueness of letters in the string but subtracting 2 to the length of the set of letters in the string (`letters_set = set(s)`). If the string is happy, all consecutive sequences of 3 letters should be unique, so the set size should be equal to the number of 3-letter sequences in the string (len(string) - 2).

The final result is returned based on the calculation of the uniqueness of letters in the string.