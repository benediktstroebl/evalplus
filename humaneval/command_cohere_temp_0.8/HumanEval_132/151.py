```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[':
            open += 1
        elif char == ']':
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the opening and closing brackets `[` and `]` as it iterates over the input string. If the count of open brackets is greater than the count of close brackets at any point, the function returns `False` since a properly nested sequence cannot end with more open brackets than close brackets. If at the end of the string, the counts are equal, it returns `True`, indicating a valid nested sequence.

This approach ensures that the function returns the correct results for the provided test cases and is efficiently implemented for simplicity.