```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the number of opening and closing brackets in the given string. The count of opening brackets should always be equal to the count of closing brackets at the correct nesting level for the function to return True. The provided tests in the code block assert this functionality.