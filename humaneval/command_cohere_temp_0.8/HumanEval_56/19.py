```python
def correct_bracketing(brackets):
    open, close = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            close += 1
        if open > close:
            return False
    return open == close
```

This script defines a function `correct_bracketing` that takes a string `brackets` as input. It counts the number of opening and closing brackets using two counters. It then iterates through each character in the string and increments the appropriate counter based on whether it's an opening or closing bracket. Finally, it checks whether the count of opening brackets is equal to the count of closing brackets. If they are equal, it returns `True`; otherwise, it returns `False`.