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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the number of opening and closing brackets within the string using two counters, `open` and `close`, which are initialized to 0. It then iterates through each character in the input string, incrementing the `open` counter if it encounters an opening bracket (`<`) and the `close` counter if it finds a closing bracket ('>'). Additionally, it checks whether the number of opening brackets is greater than the number of closing brackets during the iteration and returns `False` if this condition is detected. Finally, if the count of opening brackets is equal to the count of closing brackets when the loop finishes, it returns `True`, indicating that every opening bracket has a corresponding closing bracket in the provided string.