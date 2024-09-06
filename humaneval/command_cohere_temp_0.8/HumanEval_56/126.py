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

This script defines a function `correct_bracketing` that takes a string `brackets` as input. It counts the number of opening and closing brackets within the string using two counters. The function then compares the counts of opening and closing brackets. If the count of open brackets is greater than the count of close brackets, the function returns `False`; otherwise, it returns `True`. 

This solution ensures that every opening bracket has a chance to be matched with a closing bracket, regardless of the order of the characters in the input string. Hence it correctly solves the problem.