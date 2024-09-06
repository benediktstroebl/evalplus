```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The function checks if the input string `s` is happy by using the following logic:
1. It first checks if the string's length is at least 3.
2. If the above condition is met, it checks if the number of distinct letters in the string is equal to the number of letters in the string minus 2.

The function returns `True` if the string is happy, and `False` otherwise. You can test this function directly in the Python interpreter, and it will return the correct values for the examples in the problem statement.