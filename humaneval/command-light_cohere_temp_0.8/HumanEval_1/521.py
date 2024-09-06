```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [c for c in s if c in '()()()]

def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'])
    assert separate_paren_groups('foo Bar(((( ))b')')') == ['foo', 'Bar', '(((())b')')]
    assert separate_paren_groups('(A)BB( )')) == ['(A)', 'BB()']
    assert separate_paren_groups('( )( )') == ['()', '()()']
    assert separate_paren_groups('( (()) )') == ['()', '()()']

```
The function `separate_paren_groups` takes a string of parenthesis-delimited groups as its argument and returns a list of non-empty strings, each representing a group of parentheses. The test_separate_paren_groups function verifies that the `separate_paren_groups` function works correctly for different inputs and provides examples for how the function should behave.