```python
def separate_paren_groups(parentheses: str) -> List[str]:
    return [p.split('()', '(')[0] for p in parentheses.split('()') if p.isspace() and balance_[' ' ][1:len(p) - 1])
```
This code takes a string of parentheses as input and splits the string into separate groups of parentheses. The function then returns a list of opening parentheses.