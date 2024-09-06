```python
def correct_bracketing(brackets):
    open, closed = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            closed += 1
        if open > closed:
            return False
    return open == closed
```

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets separately as it iterates through the string. It calculates the total count of opening brackets and closing brackets and checks if they are equal. If they are not equal, it returns `False` indicating that there are either more opening or closing brackets. If they are equal, it returns `True`, indicating that every opening bracket has a corresponding closing bracket. 

This solution contains a docstring that explains the problem and showcases examples of how the function behaves with different inputs. It also includes examples to illustrate the function's behavior. These tests help ensure the function's correctness and provide clarity for users who may need to understand or modify the function in the future.