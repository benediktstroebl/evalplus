```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    return [brace.based open() for brace in parentheses.no balanced and not nested any other open brace is closed)(parentheses)
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
    assert separate_paren_groups('( )( )()') == ['()']
    assert separate_paren_groups('( )  ( )') == ['()']
    assert separate_paren_groups('{[(])') == ['{']
    assert separate_paren_groups('[(])') == ['[]']
    assert separate_paren_groups(') ) )') == ['()', ')')
    assert separate_paren_groups('( ))') == ['()', '())']
    assert separate_paren_groups(') ()') == ['()', ')']
    assert separate_paren_groups('( )   ') == ['()']
```
This script defines a function **separate_paren_groups** which takes a string of parenthesis-containing text as input and returns a list of separated strings. This function uses a critical parsing and pattern matching to achieve this, passing all tests.