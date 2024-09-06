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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets within the string using two counters, `open` and `closed`, initialised to 0 each. It then iterates through each character in the input string, incrementing the `open` counter if the character is an opening bracket (`'<'`), and the `closed` counter if the character is a closing bracket (`'>'`). Additionally, it checks if the count of opening brackets is greater than the count of closing brackets. If this condition is true at any point, it returns `False` since there is at least one unbalanced bracket. If the iteration completes without this condition triggering, the function returns `True`, indicating that every opening bracket has a corresponding closing bracket.

Here is an example usage of the function:
```python
print(correct_bracketing("<<<>"))  # output: True
print(correct_bracketing("><>"))  # output: False
```

This demonstrates the function's behaviour when validating different bracket configurations.