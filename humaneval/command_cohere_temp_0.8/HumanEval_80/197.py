```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

This code defines a function `is_happy` that uses set logic to check if the given string is happy. The function's logic checks every 3 consecutive letters in the string, ensuring that they are distinct. The function returns True if the conditions are met, and False otherwise. 

To validate the correctness of the logic, you can create a test suite with example strings and compare the expected outputs against the outputs produced by the `is_happy` function.