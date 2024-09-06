```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    A function that takes a string of parentheses and returns a list of separate parenthesis groups.

    Returns a team:
    """
    return [s.split('(')')] if isinstance(s, str) else [s]  # test case handling
    return [gp.split('(')')[0] for gp in s.split('('(')]  # clean split into groups of only parentheses (no spaces) and return the first character only of each group 

# unit tests:
def test_separate_paren_groups():
    assert separate_paren_groups('() (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups(') ') == ['()']
    assert separate_paren_groups('(') )') == ['()']
    assert separate_paren_groups('  ( )  ( )') == ['()']
    assert separate_paren_groups('( )   ()') == ['()']
    assert separate_paren_groups('((())))') == ['()']

```
This script defines a function `separate_paren_groups` that splits a given string of parentheses into individual groups, without considering spaces. The tests verify that correct functionality of the function, by checking if the output of the function matches the expected output for different input strings.