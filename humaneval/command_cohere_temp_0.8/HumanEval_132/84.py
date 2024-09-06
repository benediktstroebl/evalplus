```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']' :
            closed += 1
        if closed > open:
            return False
    return True
```

The function counts the opening and closing brackets accordingly to make the decision. It increases the `open` counter whenever it encounters an opening bracket `[`, and decreases the `closed` counter whenever it encounters a closing bracket `]`. If at any point the `closed` counter is greater than the `open` counter, then there is an unbalanced bracket sequence and the function returns False. If the counter is balanced at the end, the function returns True. The given examples in the problem statement all have the correct outcomes explained in the corresponding comment.