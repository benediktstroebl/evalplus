```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.split('('))
    close_brackets = len(brackets.split(')'))
    return open_brackets == close_brackets
```

This function directly computes the difference between the count of open versus closed brackets, stemming from the requirement of every open bracket having a corresponding closed one. The given tests pass with this implementation.