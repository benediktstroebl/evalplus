```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    for i in range(3, len(s), 3):
        if len(set(s[i:i+3])) != 3:
            return False
    return True
```

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function returns `True` if the string is happy, and `False` otherwise. 

The function first checks if the length of the string is at least 3, and every 3 consecutive letters are distinct. If these two conditions are met, the function returns `True`. If either condition is not met, the function returns `False`. 

You can use this function by calling it and passing a string as an argument to determine whether the string is happy or not. 

**NOTE:** The script assumes that the input passed is already validated to fit the problem description mentioned above.