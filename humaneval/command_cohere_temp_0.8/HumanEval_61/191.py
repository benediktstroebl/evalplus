```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.count('('))
    close_brackets = len(brackets.count(')'))
    return open_brackets == close_brackets
```

This function uses the built-in methods to count the number of opening and closing brackets and compares them, ensuring that the number of opening brackets is equal to the number of closing brackets in the given string.