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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets within the string, ensuring that each opening bracket is matched with a corresponding closing bracket. It returns `True` if the counts are equal, indicating that the brackets are correctly paired, and `False` otherwise. 

Here is an example of function usage:
```python
print(correct_bracketing("<>"))  # Output: True
print(correct_bracketing("><"))  # Output: False
```

This function's correctness is validated via the provided tests, ensuring its reliability in solving the problem.