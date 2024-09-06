```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']':
            closed += 1
        if closed > open:
            return False
    return open != 0
```

The function counts the number of open and closed brackets until it reaches the end of the string. It returns False if the number of closed brackets is greater than the number of open brackets at any point or if the string does not contain any open brackets. It returns True if at least one open bracket is nested, meaning the number of open brackets is not zero. 

To run this code the only dependency required is the Python interpreter which you can install on your machine or use an online IDE. Feel free to modify the function or the tests to fit your needs. Let me know if you have any other questions!