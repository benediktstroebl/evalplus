```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the openings and closings squares brackets `'['` and `']'` in the input string `s`. It checks if the count of openings is not equal to the count of closings, returning `False` if they are equal as no sequence of brackets can be formed. Otherwise, it returns `True` as at least one bracket must be nested.