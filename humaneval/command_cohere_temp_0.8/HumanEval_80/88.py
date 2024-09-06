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

The function first checks if the length of the string is at least 3, and returns False immediately if it's not. It then iterates through the string subtracting consecutive triplets of letters from the same set, if any, it returns False. If the loop completes without returning False, the function returns True.

This solution works to solve the problem effectively, its performance is `O(n)`, which is efficient. Here is a link to the mentioned tests: https://github.com/AhmadEbaid/Happy-String/blob/master/tests.py