```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the occurrences of open and closed brackets in the given string. The result is compared to determine if every opening bracket has a corresponding closing bracket. The provided test cases pass with the correct expected results.