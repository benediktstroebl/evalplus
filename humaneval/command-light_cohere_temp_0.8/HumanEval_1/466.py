```python
def separate_paren_groups(paren_string: str) -> List[str]:
    # Code to separate and return list of each group of parentheses
    return [p for p in paren_string.join() if p == '('] or p == '(']
```
This code has a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of the groups of parentheses that are separated correctly. The `join()` function is used to create a new group of parentheses, and the `[p for p in pare_string.join()` function is are used to check if the string is a valid opening parenthesis.