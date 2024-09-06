```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate and return groups of parentheses
    """
    return [p.replace(0, '(') + p.join(1) + ')', p.pop(1)) for p in s.pop() if p.isalpha()]
 inner = p[0:1]
    outer = p[1:]
    return [inner, outer]
# Tests
def test_separate_paren():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
```