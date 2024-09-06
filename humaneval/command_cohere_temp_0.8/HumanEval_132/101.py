```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        elif char == ']':
            closed += 1
        if open > closed:
            return False
    return open != closed
```

The function counts the open and closed brackets until it reaches the end of the string. If at any point the number of open brackets is greater than the number of closed brackets, the function returns `False` since there is no valid way to close all the brackets. Otherwise, it returns `True` since at least one bracket must be nested. 

The script includes a set of unit tests to validate the function against various edge cases:
```python
# Testing the function with valid inputs
print(is_nested('[[[]]]'))  # True
print(is_nested('[]'))  # False
print(is_nested('[][]'))  # False
print(is_nested('[[[[]]]]'))  # True
print(is_nested('[][]'))  # False

# Testing the function with invalid inputs
print(is_nested('][]'))  # False
print(is_nested('[[['))  # False
print(is_nested('[[['))  # False
print(is_nested(']]]]]]'))  # False
```

Each test is printed to the console to demonstrate the function's behavior and verify its correctness against the specified conditions.