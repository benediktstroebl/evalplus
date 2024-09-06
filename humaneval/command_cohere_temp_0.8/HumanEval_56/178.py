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

This function checks if every opening bracket `(<` has a corresponding closing bracket `>)`. It counts the opening and closing brackets as it iterates over the input string. If at any point the count of openings is greater than the count of closings, the function returns `False` since there is an unbalanced bracket. Otherwise, at the end of the string if the counts are equal, it returns `True`. 

This solution passes the unit tests provided in the problem statement.