```python
def separate_paren_groups(parentheses: str) -> List[str]:
    result = []
    for group in parentheses:
        if ')' in group:
            result.append('(')
        if '(' in group else group + ')'
        else
            result.append(group)
    return result
```
Do you need help with anything else?