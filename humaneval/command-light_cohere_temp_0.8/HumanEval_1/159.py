```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate and return groups of parentheses.
    >>> separated = separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def is_group(char):
        return char == '(' or char == ')'

    return [char for char in s if is_group(char)]

# Test cases
def test_separate_paren():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
    assert separate_paren_groups('( ) (( (( )) )) )')') == ['()', '(())', '(()())']
    assert separate_paren_groups(') )') == ['()']
    assert separate_paren_groups(' (() )') == ['()']
    assert separate_paren_groups(') (( ( ) )')') == ['()', '()()']
    assert separate_paren_groups('( )( ) ( ) ())') == ['()()']
```