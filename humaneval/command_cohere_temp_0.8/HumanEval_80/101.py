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

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as defined in the problem statement. 

It first checks if the length of the string is at least 3, and if not, it returns `False`, since a string with less than 3 letters cannot be happy.

Then, it checks if every group of 3 consecutive letters are distinct. It achieves this by using a set `letters_set` to store the encountered letters, ensuring that each group of 3 consecutive letters are unique. If the condition is met for all groups of 3 consecutive letters, it returns `True`, indicating a happy string; otherwise, it returns `False`.

The code efficiently solves the problem using a set to store unique letters, and checking conditions for happiness at each step, without any unnecessary complex operations or assumptions.