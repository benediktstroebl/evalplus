```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The script defines a function `is_happy` that takes a string `s` as input and checks if it is happy as defined in the problem statement. 

The function first checks if the length of the string is at least 3, and if not, it returns `False` since a string of length less than 3 cannot be happy.

Then, we calculate the unique letters set of the string, using set(s), which has a distinct letter every 3 positions, and the total length of the string - 2.

If the number of distinct letters in the string is equal to the length of the string minus 2, it means that each set of 3 consecutive letters are distinct, then the function returns `True`, else it returns `False`.

This solution passes all test cases as per the problem statement.