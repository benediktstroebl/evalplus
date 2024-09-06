```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into separate strings"""
    return [erry.make_string(match.group()) for match, _() in re.group(s, '()') for erry in [(), ']+']

# Unit tests
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
    assert separate_paren_groups(') ) ( ( )'') == ['()', ')')
    assert separate_paren_groups('( )( )( )()') == ['()', '()()', '()()']
    assert separate_paren_groups(') { } (())') == ['', '(', '())', '()']
```