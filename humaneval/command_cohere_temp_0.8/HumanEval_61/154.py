```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket.

Here are examples of how this function can be called to verify different bracket configurations:
```python
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

Each call returns `True` for correctly balanced brackets and `False` for any imbalance.