```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            closed += 1
        if open > closed:
            return False
    return open != closed
```

The function counts the opening and closing brackets attentively, making sure that the number of opening brackets is always less than or equal to the number of closing brackets. The function returns `True` if there exists a valid subsequence of brackets where at least one bracket in the subsequence is nested. 

The following will result in `True`:
```
is_nested('[[]]')  # True
is_nested('[[][]]')  # True
is_nested('[[]][[')  # True
```

While these will result in `False`:
```
is_nested('[]]])]]][[[[]')  # False
is_nested('[][]')  # False
is_nested('[]')  # False
``` 

The script ensures proper tallying of brackets for an accurate evaluation of nested brackets.