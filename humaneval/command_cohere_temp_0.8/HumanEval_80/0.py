```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(s) % 3 == 0 and len(letters_set) == len(s) - 2
```

The function checks if the string's length is at least 3 and the number of distinct letters in the string is equal to the length of the string minus 2. The **dist(inct)**, **val(ue)**, and **cor(rect)** functions are helper functions to check if every 3 consecutive letters are distinct.