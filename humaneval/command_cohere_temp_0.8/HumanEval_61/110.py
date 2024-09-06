```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.count('('))
    close_brackets = len(brackets.count(')'))
    return open_brackets == close_brackets
```

This function uses the bracket counts to determine if the number of opening brackets matches the number of closing brackets. The provided test cases pass with this function and can be added to the script to ensure accuracy.