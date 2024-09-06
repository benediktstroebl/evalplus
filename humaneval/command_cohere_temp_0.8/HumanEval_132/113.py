```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[':
            open += 1
        elif char == ']':
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the openings '[' and closings ']' using two counters. The solution is a simple imbalance check of these counters. An opening bracket '[[' can only be balanced by a closing bracket ']]'. The provided solution uses a single counter for each, updating them based on the encountered characters and returning True if the counter imbalance is only due to nested brackets. It returns False if there is an imbalance and the string does not have a valid subsequence of nested brackets.