```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the occurrences of "(" and ")" in the `brackets` string. It then compares these counts to confirm if each opening bracket has a corresponding closing bracket. The provided test cases demonstrate the function's behavior for various input scenarios.