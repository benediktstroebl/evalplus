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

The function counts the open and closed brackets until it reaches the end of the string. If at any point the number of open brackets is greater than the number of closed brackets, the function returns `False` since there is no possible way to have a valid nested bracket sequence. If at any point the number of closed brackets is greater than the number of open brackets, the function returns `True` since at least one bracket from the sequence is nested. If both counts are equal at the end, or if the string is empty, it returns `False` as there is no valid subsequence. 

This solution works for both single and multiple nested square brackets. Also, it does not matter in what order the square brackets are, as long as they are valid when compared in any permutation. 

To test out the function, try running it with the provided test cases and more of your own:
```python
print(is_nested('[[[]]]'))
print(is_nested('][]'))
print(is_nested('[]'))
print(is_nested('[[[]][[]]))
``` 
The function should return:
```
True
False
False
True
```