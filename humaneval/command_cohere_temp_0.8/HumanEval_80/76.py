```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
            return False
    return True
```

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as described in the problem statement. 

It first checks if the length of the string is at least 3, and if not, it returns `False`, since a string with less than 3 letters cannot be happy.

Then, it uses a set called `letters_set` to store the letters encountered as it iterates through the string. By using a set, we can quickly check if any duplicates occur. It iterates through the string with steps of 3, and for each window of 3 letters, it checks if they are unique. If they are not unique (i.e., the set length is not 3), it returns `False`. Otherwise, it returns `True`.

This code can be used as a standalone module to check if a given string is happy, as per the problem statement. You can use it by calling `is_happy(s)` with a string `s`, and it will return `True` if the string is happy, and `False` otherwise.