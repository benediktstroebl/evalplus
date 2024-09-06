```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The function checks if the provided string is happy by using set theory. It initializes a set to store the letters of the input string, then checks if the set's length is equal to the number of distinct letters in the string minus 2. This is an efficient way to determine if all three-letter combinations are unique in the string.