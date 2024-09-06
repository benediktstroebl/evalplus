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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets separately as it iterates through the string. It keeps track of the imbalance of open and closed brackets and returns False if there is an imbalance at any point. It returns True only if there are the same number of opening and closing brackets.