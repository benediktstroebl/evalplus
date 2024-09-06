```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The script defines a function `is_happy` that takes a string `s` as input and checks if it is happy as defined in the problem statement. 

The function first checks if the length of the string is at least 3, and if not, it returns False, since a string of length less than 3 cannot be happy.

If the string length is at least 3, it proceeds to calculate the number of unique letters in the string, by converting the string to a set and getting its size. This is done using the `set()` function which removes duplicate letters, and the `len()` function which calculates the size of the set. The number of unique letters in the set is expected to be equal to the length of the input string minus 2, as for every 3 consecutive letters, there will be one unique letter and two separators. 

If the number of unique letters is equal to the length of the string minus 2, the function returns `True`, otherwise it returns `False`. 

The script proposes a clean and efficient way to tackle the problem with the use of sets and proper checks for edge cases. 

To see this code in action, you can run it in your Python interpreter.