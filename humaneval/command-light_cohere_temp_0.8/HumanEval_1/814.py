```python
def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    for group in paren_string.split(' ')+'):
        if group: # remove empty string
            result.append('(' + group + ')')
    return result
```  This code splits the string around spaces into list elements and removes empty elements.