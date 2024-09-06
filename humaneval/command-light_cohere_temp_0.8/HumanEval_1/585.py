```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p.format("({})", s) for p, s in zip('(' * s + ')', s.replace('\n', )))
def test_function():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'])
    assert separate_paren_groups('( )- (( ))') == ['()', '-()')
    assert separate_paren_groups('( ( ) ) (( ))') == ['()', '()()', '()()]
    assert separate_paren_groups('(( ((() ) ) ) )') == ['((())())')']
    assert separate_paren_groups('( )  ( )  ( )') == ['()', '()()]')
``` 
The function 'separate_paren_groups' accepts a string containing multiple groups of parentheses, and returns a list of separated strings. The 'test_function' section provides test cases to check the correctness of the 'separate_paren_groups' function.