```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into separate strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    for match in s.match.iter():
        open:
        result.append(match.group().
    return result

        if not isinstance(result, List):
            raise TypeError("Expected a list")
    return result
```