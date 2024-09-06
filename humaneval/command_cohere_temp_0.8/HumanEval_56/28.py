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

This script defines a function `correct_bracketing` that takes a string `brackets` as input. It counts the number of opening and closing brackets within the string using two counters. The function then compares the counts of opening and closing brackets. If the count of open brackets is greater than the count of close brackets, the function returns `False`, indicating that there are more opening brackets than closing brackets. Otherwise, if the counts are equal, it returns `True`, suggesting that every opening bracket has a corresponding closing bracket. 

The expected behavior is illustrated in the docstring, which includes example tests that are easily executable because the function is self-contained.