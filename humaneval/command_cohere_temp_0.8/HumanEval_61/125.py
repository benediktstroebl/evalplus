```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of '(' and ')' characters in the `brackets` string using the `count` method. It then compares the counts of both types of brackets to determine if every opening bracket has a corresponding closing bracket, and returns a boolean value accordingly.