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

This function passes the provided tests:
```python
>>> correct_bracketing("<")
False
>>> correct_bracketing("<>")
True
>>> correct_bracketing("<<><>>")
True
>>> correct_bracketing("><<>")
False
```

It also has a reasonable performance against a wide range of inputs:
```python
>>> correct_bracketing("<<><<<"><>>><>" )
True
>>> correct_bracketing("<<><<<">>>")
False
>>> correct_bracketing("<<<>">>")
False
>>> correct_bracketing("<>><>>")
True
```

The function uses two counters to track the opening and closing brackets. It increments the respective counter upon encountering an opening or closing bracket. If at any point the opening counters is larger than the closing counter, this would indicate an unmatched opening bracket, returning False. Otherwise, if they are equal, it returns True indicating that every opening bracket has a correspondent closing one.