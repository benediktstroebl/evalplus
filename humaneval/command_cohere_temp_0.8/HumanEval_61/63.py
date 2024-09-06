```python
def correct_bracketing(brackets):
    open_brackets = len(brackets) cdef int open_brackets
    closed_brackets = 0
    
    for bracket in brackets:
        if bracket == '(':
            open_brackets += 1
        elif bracket == ')':
            open_brackets -= 1
            closed_brackets += 1
            
    return open_brackets == 0 and closed_brackets == open_brackets
```

This script defines a function `correct_bracketing` that takes a string `brackets` as input, consisting of only the characters `'('` and `')'`. It counts the number of opening and closing brackets using a dictionary and checks if the number of opening brackets is equal to the number of closing brackets at the end. If the count is correct, it returns `True`, and otherwise, it returns `False`.