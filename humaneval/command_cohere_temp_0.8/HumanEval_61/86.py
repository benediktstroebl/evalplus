```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function uses the `count` method to check for the opening and closing brackets and returns True if they are equal. It returns False if there is any discrepancy between the counts.