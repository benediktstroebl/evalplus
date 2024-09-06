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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the number of opening and closing brackets within the string using two counters, `open` and `close`, which are initialized to 0. It then iterates through each character in the input string and increments the `open` counter if the character is an opening bracket (`'<'`) and the `close` counter if the character is a closing bracket (`'>'`). Additionally, it checks whether the count of opening brackets is greater than the count of closing brackets during each iteration to ensure that all opening brackets are properly closed. Finally, the function returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket, and `False` otherwise.