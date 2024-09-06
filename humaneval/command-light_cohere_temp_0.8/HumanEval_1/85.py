```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [ Pops() for Pops in (p for p in s if not p == ' ') ]
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('( ) -( )') == ['()', ' -(']
    assert separate_paren_groups('( )( )-( )') == ['()', '( )( )-']
    assert separate_paren_groups('( )( )()') == ['()', '( )()']
    assert separate_paren_groups('<(>)') == ['<']
    assert separate_paren_groups('> <(())') == ['>', '<(']
    assert separate_paren_groups('(())') == ['(', ')']
    assert separate_paren_groups('  ( )') == ['(']
    assert separate_paren_groups('{ ) }') == ['{', '}']
def Pops():
    s = input()
    return s.pop(0)
``` 
This code defines a function called `Pops` which pops the last character from the string `s` (taken from the input), and returns it. It is also defines a `test_separate_paren_groups` function that tests the correctness of the `separate_paren_groups` function.