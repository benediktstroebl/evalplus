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

The function counts the opening and closing square brackets and checks if they are balanced. It returns False if there is an imbalance at any point or if there is never an imbalance. Otherewise, it returns True which indicates the presence of at least one nested bracket.