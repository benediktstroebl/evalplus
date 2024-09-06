```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p for p in s.string() if p != ')']

def test_function() -> None:
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
    assert separate_paren_groups('( ) (( ) ) )')') == ['()', '( )', '()()']
    assert separate_paren_groups('( ) ( ) )') == ['()', '()']
    assert separate_paren_groups('( ) )') == ['()']
    assert separate_paren_groups('( bar ))') == ['()', 'bar']
    assert separate_paren_groups(') )') == []
``` 
This script defines a function `separate_paren_groups` that takes a string as input and returns a list of parenthesis-free strings. It also includes a test function that tests the `separate_paren_groups` function with various input strings.