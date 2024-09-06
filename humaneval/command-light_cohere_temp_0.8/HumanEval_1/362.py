```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    return [p.split('() for p in parentheses.
    )
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'])
    return
    assert separate_paren_groups('((()))') == ['()', '()()']
    assert separate_paren_groups(') ) }') == ['()', ')']
    assert separate_paren_groups(') } }') == ['()', '}']
    assert separate_paren_groups('} } }') == ['}']
    assert separate_paren_groups(') { }') == ['()', '}']
    assert separate_paren_groups('} { (') == ['}']
    return
```