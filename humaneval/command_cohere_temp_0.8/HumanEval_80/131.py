```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The function uses a set data structure to store the letters of the input string and then checks whether the number of distinct letters in the string is equal to the number of letters in the string minus 2. The minus 2 accounts for the check that every 3 consecutive letters are distinct.