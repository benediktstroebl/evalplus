```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i+1], s[i+2]])) != 3:
            return False
    return True
```

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function first checks if the length of the string is equal to or greater than 3. If not, it returns False, since the string cannot be happy. Then, it iterates over the string skipping every two letters, and if any consecutive trio of letters is not distinct, the function returns False. Otherwise, it returns True.