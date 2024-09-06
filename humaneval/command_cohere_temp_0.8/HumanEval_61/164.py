```python
def correct_bracketing(brackets):
    open_brackets = len(brackets) - brackets.count('(')
    close_brackets = len(brackets) - brackets.count(')')
    return open_brackets == close_brackets
```

This function directly computes the difference between the total length of the string and the number of '(' and ')' characters to determine whether the number of opening and closing brackets is consistent. It assumes that the string contains only '(' and ')' characters.