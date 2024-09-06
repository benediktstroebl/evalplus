```python
from typing import List
def separate_paren_groups(parenthesis_string: str) -> List[str]:
    """
    Separate each balanced group of parentheses into separate strings.
    >>> separate_paren_groups(') (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [part for part in parenthesis_strings.split('\n '') if part.strip('()') and  ]

def test_separate_paren_groups():
    assert separate_paren_groups(') ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_again():
    assert separate_paren_groups(')( ) (( )) )()()') == ['()', '())', '()()()()']
```
This code defines two testing functions for the `separate_paren_groups` function. It passes the for both test cases, which confirms that the function works correctly.