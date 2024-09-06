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

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function first checks if the length of the string is equal to or greater than 3. If not, it returns False, since the string cannot be happy. Then, it iterates over the string checking if any triple of consecutive letters appears more than once. If this is the case, it returns False, if not it returns True. 

You can use it in your problem statement to check if a given string is happy or not. Let me know if it works!