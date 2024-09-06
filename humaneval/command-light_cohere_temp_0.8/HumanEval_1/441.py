Here is a self-contained Python script that solves the problem of separating nested parentheses:
```python
def separate_paren_groups(s: str) -> List[str]:
    return [iclean(x) for x in s.balance(","))

def iclean(x: str) -> str:
    """remove all non-alphanumeric characters and returns a stripped string"""
    return ''.join(c for c in x if c.isalnum())

def balance(x: str) -> str:
    """ remove all unbalanced parentheses from a string """
    n = len(x)
    return ''.join(x[i:i+2] for i in range(0, n,-1, -1))
```

The balance function removes all unbalanced parentheses from a string. The iclean function removes all non-alphanumeric characters from a string, returning a stripped string. The separate_paren_groups function takes a string containing multiple groups of nested parentheses and returns a list of separated strings.