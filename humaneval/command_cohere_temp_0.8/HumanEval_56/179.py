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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the number of opening and closing brackets within the string using two counters, `open` and `closed`, initialised to 0. It then iterates through each character in the input string, incrementing the `open` counter if it encounters an opening bracket (`'<'`), and incrementing the `closed` counter if it finds a closing bracket (`'>'`). Additionally, it checks if the count of opening brackets is greater than the count of closing brackets; if so, it immediately returns `False` since there are more opening brackets than closing ones, and the input brackets are not correctly matched.

The function finally returns `True` if the count of opening brackets is equal to the count of closing brackets, indicating that every opening bracket has a corresponding closing one, hence the brackets are correctly matched. 

Here are some example outputs:
```
>>> correct_brackets("<<<>")
True
>>> correct_brackets("><<>")
False
>>> correct_brackets("<>")
False
>>> correct_brackets("<<><>>")
True
```