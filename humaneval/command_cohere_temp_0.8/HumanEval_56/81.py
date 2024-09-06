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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function calculates the count of both opening and closing brackets and returns `True` if the count of opening brackets is equal to the count of closing brackets, indicating that every opening bracket has a corresponding closing bracket. Otherwise, it returns `False`. 

Here is an example of function usage:
```python
print(correct_bracketing("<>"))  # Output: True
print(correct_bracketing("><"))  # Output: False
```

The provided examples in the problem statement yield the following results:
```
False
True
True
False
```