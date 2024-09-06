```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    return [p for p in parentheses.
    if p and ')' in parenthesis:
        p = p.replace(')', ')'
    else:
        p = p.replace('(', ')', '')
    return [p for p in parentheses if p]
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
    assert separate_paren_groups('()' == '()') == ['()']
    assert separate_paren_groups('( )( )') == ['()', '()']
    assert separate_paren_groups('(()))()') == ['()', '()']
    assert separate_paren_groups('() ( )') == ['()', '(']
    assert separate_paren_groups(') ) ( )') == ['(']
    assert separate_paren_groups(') ( ( ) )') == ['(', ')']
```