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

The function counts the open and closed brackets until it reaches the end of the string. If at any point the number of open brackets is greater than the number of closed brackets, the function returns `False` because there are insufficient closed brackets to match the open brackets, and vice versa. The function returns `True` when both count the same or when one of them is zero (i.e. the number of open and closed brackets is balanced but not necessarily nested). 

The markdown code block explains how the code works and includes a unit test that can verify the result:
```python
assert is_nested("[]") == False
assert is_nested("[]}") == False
assert is_nested("[[[]]])") == False

assert is_nested("[[[])]]") == True
assert is_nested("[[[]][[]]])") == True
assert is_nested("[[[[[[[]]]]]]]") == True
``` 

The test cases cover various edge cases and different sequences of brackets to validate the behavior of the `is_nested` function.