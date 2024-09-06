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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets within the string using two counters, `open` and `closed`, initialised to 0 each. It then iterates through each character in the input string, incrementing the `open` counter if the character is an opening bracket (`'<'`), and the `closed` counter if the character is a closing bracket (`'>'`). After processing all characters, the function compares the counts of opening and closing brackets. If the count for opening brackets is greater than the count for closing brackets, it returns `False` as not all opening brackets have corresponding closing brackets. If the counts are equal, it returns `True`, indicating that every opening bracket has a corresponding closing bracket in the given string.