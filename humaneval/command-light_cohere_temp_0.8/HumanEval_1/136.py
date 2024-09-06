```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate balanced parentheses from a string.
    Returns list of balanced parentheses.
    """ Tests with strings containing balanced parentheses.
    """
    example input: )(()())((())
    """
    return ['\n' if '(' == s[0] and s[1] == ')' else s for i, s[i] == '(' or ')'
        while i < len(s) and s[i] == '(' or s[i] == ')': i += 1
        return ['', '('] + separate_paren_groups(s[i:]) for i in range(len(s)-1)]

def test_separate_paren_groups():
    assert separate_paren_groups(') ) (( )) (( )( ))' == ['\n', '()', '(()')']
    assert separate_paren_groups(') )') == ['\n', '()']
    assert separate_paren_groups('( )') == ['()']
    assert separate_paren_groups('() )()') == ['()()']
    assert separate_paren_groups('()(((((()))))-') == ['()()']
```