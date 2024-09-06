```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']' :
            close += 1
        if open > close :
            return False
        open -= 1
        close -= 1
    return True
```

The function counts the opening and closing brackets iterating through the characters of the input string. It returns `True` if at any moment the number of opened brackets is greater than the number of closed ones, otherwise, it returns `False`.