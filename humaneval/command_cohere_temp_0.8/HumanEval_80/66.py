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

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function first checks if the length of the string is equal to or greater than 3. If the length is less than 3, it returns `False` as happy strings must have a length of at least 3. Then, it iterates through the string subtracting consecutive letters from a set to check if they are distinct. If the set length is not equal to 3 for any iteration, it returns False. Otherwise, it returns True.

The script passes the test cases provided in the original prompt and should provide True for valid happy strings and False otherwise.