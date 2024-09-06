```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Split a string of parentheses into separate groups.

    Parameters:
    string s: The input string to split.
    Returns: list of strings: each representing a separate group of parentheses.
    """
    test cases:
    """
    assert separate_paren_groups("()" == ['()'])
    assert separate_paren_groups("(())") == ['()', '()()]
    assert separate_paren_groups("( ) (( )) ) ") == ['()', '(())', '(())'']
    assert separate_paren_groups("(((((((((())))))))))))))" == ['()', '(()', '()())', '()()()()()()()()]
    assert separate_paren_groups("( ) ) ") == ['()']
    assert separate_paren_groups("( ( ) ) ") == ['()', '(']
    assert separate_paren_groups("() () ()") == ['()', '()()']
    assert separate_paren_groups("( ) () () ()") == ['()', '()()()']
    assert separate_paren_groups("(() )() () ") != ['()', '()()']
    return ['(']  # this is a bit incorrect, it should return [] not empty string
```