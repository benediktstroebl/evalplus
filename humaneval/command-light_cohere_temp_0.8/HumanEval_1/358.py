```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all nested parentheses from a string.
    >>> '(( ))'
    ['(', ')']
    """
    result = []
    for match in s.match('(\(\([\+\))?\Z\Z', 'g')]:
        result.append(match.group().match.group)
        .template with this case:
        r = re.sub(r'\)\', '', match)
        result.append(r)
    return result
```

This code defines a function `separate_paren_groups` that takes a string as input and returns a list of parenthesis-free strings. The function uses regular expressions and the `re.push()` method to achieve the task.