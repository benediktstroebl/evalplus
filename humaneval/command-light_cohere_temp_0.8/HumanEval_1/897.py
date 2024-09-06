```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all spaces around parentheses and separate each group into a separate string.
    """
    opening_braces and closing_braces: [{}], [)]
    """
    return [brace.join(' ' ') for brace in s.join('{', '}', '(', ')', '[', ']')]
# Tests
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
    assert separate_paren_groups(' ( )') == ['()']
    assert separate_paren_groups(' ( ((( )) )  )') == ['()']
    assert separate_paren_groups('(( (( (())))' ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('( )( )()') == ['()()']
    assert separate_paren_groups('  ( )  ( )  )  ') == ['()']
    assert separate_paren_groups('  ( )   ( )  )  ') == ['()']
    assert separate_paren_groups('  (( ))   ( )  )  ') == ['()', '()']
```  This code defines a function called `separate_paren_groups` that takes a string as input and returns a list of strings with balanced parentheses. The tests verify the use the basic and advanced cases for the function.