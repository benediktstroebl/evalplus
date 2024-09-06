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

The function first checks if the length of the string is at least 3, and returns `False` if it's less than 3 since a string of less than three letters cannot be happy. Then, it loops through the string minus the last two letters, and for each iteration, it checks if the combination of the three consecutive letters is unique. The function returns `False` if any of these triples are not unique, indicating that the consecutive letters are not diverse. If the loop completes without finding any repeated triples, the function returns `True`, indicating that the string is happy. 

Overall, this code correctly solves the problem and provides a self-contained implementation that can be easily used in other projects.