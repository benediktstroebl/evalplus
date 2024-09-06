```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Function to separate groups of balanced parentheses from the input string.
    Input:s are a string containing multiple groups of nested parentheses.
    Returns: list of separated strings with balanced parentheses.
    """
balanced groups of parentheses are defined as:
        ( )
       ()
      ( )
    """
    return [
        s.replace(p for p in '()'.split())
        for p in s.split('() +')
    newline
    for _ in [1,0]
    ]

def test_separate_paren():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
```