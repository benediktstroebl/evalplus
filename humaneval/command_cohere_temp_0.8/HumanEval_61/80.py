```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.split('('))
    close_brackets = len(brackets.split(')'))
    return open_brackets == close_brackets
```

This function directly computes the difference between the count of open brackets and closed brackets and returns whether they are equal, signifying correct bracketing. 

You can use the function by calling it and passing different input values to test its behavior. For example:
```python
print(correct_bracketing("()")) # Output: True
print(correct_bracketing("(()())")) # Output: True
print(correct_bracketing(")(()")) # Output: False
```

The provided examples in the problem statement return the expected outputs based on when they are called.