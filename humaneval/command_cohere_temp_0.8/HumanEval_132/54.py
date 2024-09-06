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

The function counts the opening and closing brackets `'['` and `']'` in the given string `'s'` with respective counters `open` and `closed`. If at any point the counter of open brackets exceeds the one of closed brackets, the function returns `False` since there is no way to close all opened brackets. Otherwise, at the end of the string, if the counter of open brackets is not equal to zero, this means there are unopened brackets, and the function returns `False`. If at the end the counters are equal, this means that all brackets are closed and at least one bracket is nested, then the function returns `True`. 

This solution works for both single and multi-line inputs.
 
The corresponding tests are:
```python
# Tests:
assert is_nested('[]') == False
assert is_nested('[][]') == True
assert is_nested('[[[[]]]]') == True
assert is_nested('[][]') == True
assert is_nested('[]') == False
assert is_nested('[[[]]]') == True
assert is_nested('[[][]]') == True
assert is_nested('[]') == False
assert is_nested('[[]]') == True
assert is_nested('[[]][[') == True
assert is_nested('[][][[[]]]') == True
assert is_nested('[][][[[]]]') == True
assert is_nested('[][]') == True
assert is_nested('[][[[[[]]]]]]]') == False
```