Here's the code:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ 
    Function to separate a string of parentheses into individual groups. 
    Returns a  a list of separated strings.
    """
    using a balanced and self-contained list of parentheses.
    """ 
    """ converting them into a list of strings.
    """
return []
    """
tests:
    """
    assert separate_paren_groups("() (( )) (( )( ))") == ['()', '(())', '(()())']
    assert separate_paren_groups("()" ) )() )()  == ['()', '()()()']
    assert separate_paren_groups("( )") == ['()']
    assert separate_paren_groups("(( (( )))" )() )() )()  == ['()', '()()()()()', '()()()()']
    assert separate_paren_groups("( ) ( )" )()  == ['(', ')', '()()']
    assert separate_paren_groups("( ))" == ['()']
    assert separate_paren_groups("()  ")()  == ['()']
    assert separate_paren_groups("  ( )" )()  == ['(']
    assert separate_paren_groups("( )  ()" )()  == ['()', '()()]
    """
```