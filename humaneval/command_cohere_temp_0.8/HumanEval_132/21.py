```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            closed += 1
            if open == 0:
                return False
    return closed > open
```

The function counts the opening and closing brackets accordingly to validate the requirement of having at least one nested bracket. It returns false immediately when a closing bracket occurs while the count of opening brackets is not zero. It does not require additional iterations over the string to optimize complexity, making it efficient to get the result for large inputs.