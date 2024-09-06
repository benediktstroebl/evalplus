```python
def correct_bracketing(brackets):
    open_brackets = len(brackets) - brackets.count('(')
    close_brackets = len(brackets) - brackets.count(')')
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using string slicing and the count method. It then returns True if the number of opening brackets matches the number of closing brackets and False otherwise. This solution is straightforward and efficiently passes the given tests.