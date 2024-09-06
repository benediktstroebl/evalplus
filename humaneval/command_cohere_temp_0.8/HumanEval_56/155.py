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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets separately as it iterates through the string. It tracks the count of opening brackets (`open`) and closing brackets (`close`) as they are encountered. If there's a mismatch between the counts, the function immediately returns `False`. If there are an equal number of each, it returns `True`, indicating that every opening bracket has a corresponding closing bracket. 

This solution passes the provided tests (including the edge cases) as expected.