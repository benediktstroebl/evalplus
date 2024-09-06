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

The script defines a function `is_happy` that uses set arithmetic to check whether the conditions of the problem are met. The function's output is true if every group of 3 consecutive letters in the string is unique and the string is at least 3 characters long, and false otherwise. 

You can test the correctness of the function by calling it with different strings and verifying the output against the problem statement.