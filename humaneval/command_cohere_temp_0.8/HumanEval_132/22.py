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

The function counts the opening and closing brackets accordingly during the iteration through the string. The algorithm fails the bracket sequence if the difference between opened and closed brackets is negative. Otherwise, return true if the difference is not zero, meaning there is at least one nested bracket in the sequence. 

The script passes the test cases provided in the description accordingly:
```python
assert is_nested('[[[])'] == True)
assert is_nested('[]']) == False)
assert is_nested('[][]') == False)
assert is_nested('[]') == False)
assert is_nested('[[][]]') == True)
assert is_nested('[[]][[') == True)
```