```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of well-formed parentheses.
    Return a groups as a list of strings.
    >>> s = '(())'
    groups = separate_paren_groups(s)
    assert len(groups) == 3
    assert groups[0] == '('
    assert groups[1] == '())'
    assert groups[2] == '()()'
    return groups
```