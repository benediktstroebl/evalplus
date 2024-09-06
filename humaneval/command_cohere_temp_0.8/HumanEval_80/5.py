```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(s) % 3 == 0 and len(letters_set) == len(s) - 2
```

The function uses an interesting approach. At first, we check if the length of the string is at least 3 to ensure the basic requirement is met. Then, we use a set to store the letters, and systematically check if every 3 consecutive letters are distinct. The resulting set size equals the number of different letters in the string, minus 2 (as the first and last letters are not part of any consecutive triple). Hence, a happy string has a length that's divisible by 3 and a set of letters with 2 elements - which translates to the happy result.