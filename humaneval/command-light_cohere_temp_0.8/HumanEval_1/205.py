```python
def separate_paren_groups(s: str) -> List[str]:
    inside = []
    pairs = []
    for w in s:
        if w == '(':
            inside.append(')')
        else:
            pairs.append(inside.append(w))
            inside = []
    pairs.append(')')
    return pairs
```