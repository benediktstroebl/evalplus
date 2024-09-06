```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the occurrences of open and closed brackets in the given string. The correctness of each test case is then determined by comparing these counts.