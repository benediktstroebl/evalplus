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

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function returns `True` if the string is happy, and `False` otherwise. 

The function first checks if the length of the string is at least 3, and every 3 consecutive letters are distinct. If these two conditions are met, then the function returns `True`. Otherwise, it returns `False`. 

This solution adheres to the problem statement, and should therefore pass any tests correctly formulated alongside it.