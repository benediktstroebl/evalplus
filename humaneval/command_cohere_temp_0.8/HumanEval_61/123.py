```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the number of opening and closing brackets in the given string. The function then returns `True` if the counts are equal and `False` otherwise.