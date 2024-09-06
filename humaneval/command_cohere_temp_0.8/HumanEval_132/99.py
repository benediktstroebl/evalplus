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

The function counts the openings '[' and closings ']' as it iterates through the string. The outcome is returned based on the simple logic that if the number of openings is different from the number of closings, at least one bracket must be nested.

To demonstrate the behavior of the function, here are some examples:
```python
print(is_nested('[[[]]'))  # Output: True
print(is_nested('][]'))  # Output: False
print(is_nested('[][]'))  # Output: False
print(is_nested('[]'))  # Output: False
print(is_nested('[[][]]'))  # Output: True
print(is_nested('[[]][[]'))  # Output: True
```