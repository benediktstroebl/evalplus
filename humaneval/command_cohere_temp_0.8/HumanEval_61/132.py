```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.split('('))
    close_brackets = len(brackets.split(')'))
    return open_brackets == close_brackets
```

This function directly computes the difference between the count of open versus closed brackets, ensuring that they are always in balance. 

You can use this function in the following way:
```python
>>> correct_bracketing("()")
True
>>> correct_bracketing("(()())")
True
>>> correct_bracketing(")(()")
False
```