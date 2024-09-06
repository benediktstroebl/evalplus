```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']':
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the openings and closings squares brackets `'['` and `']'` in the input string `s`. When the function finds a closing bracket `']'`, it checks if there is a corresponding opening bracket `'['` and vice versa. If at any moment the number of opening brackets differs from the number of closing brackets, the function returns `False`. If the final count of openings and closings is the same, it means that there is at least one correctly nested sequence of brackets, and the function returns `True`.