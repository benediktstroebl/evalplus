```python
def separate_paren_groups(s: str) -> List[str]:
    return [p.split('(',') for p in s.split(' ')]

def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('( ) ( ) (( ))') == ['()', '()()()', '()()]
    assert separate_paren_groups('( ) (( ) )') == ['()', '()()', ')')
    assert separate_paren_groups('( )( )( ) ( )') == ['()', '()', '()']
    assert separate_paren_groups('{ ) }') == ['{', '}']
    assert separate_paren_groups(') ) }') == ['()', '}']
    assert separate_paren_groups('( ) ( })') == ['()', ')']
    assert separate_paren_groups('( ) } (')) == ['()', ' }']
    assert separate_paren_groups(' ( )   ()') == ['()', '()']
```
The provided Python code defines a function `separate_paren_groups` that splits a given string into a list of separate parenthesis groups. 

The `test_separate_paren_groups` function contains several assertions that verify the correctness of the `separate_paren_groups` function by testing different input strings.