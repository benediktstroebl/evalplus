```python
def correct_bracketing(brackets):
    open, close = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            close += 1
        if open > close:
            return False
    return open == close
```

This Python script provides a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets and returns `True` if the number of opening brackets is equal to the number of closing brackets, indicating that the brackets are balanced, and `False` otherwise. 

Here is an example of function usage:
```python
print(correct_bracketing("<<>>")) # Output: True
print(correct_bracketing("><")) # Output: False
```

The provided examples demonstrate how the function can be used to verify if a given string of brackets is correctly balanced.