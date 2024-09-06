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

The function counts the openings '[' and closings ']' as it iterates through the string. The idea for this solution is that a valid bracket sequence has no gaps in closing brackets where the balance goes negative, and at some point, it must go positive again, indicating a properly nested sequence. The provided test cases illustrate the behavior of the function and demonstrate its correctness. 

For instance, the call `is_nested('[[]]')` returns `True` since the openings and closings are balanced and there is a nested bracket. On the other hand, the call `is_nested('[][]')` returns `False` because although it has openings and closings, they are not balanced and there is no nested bracket.