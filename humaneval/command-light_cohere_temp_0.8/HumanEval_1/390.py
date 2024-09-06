```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses
    Return a list of separated strings
    Returns: list of strings, each representing a balanced group of parentheses"""
    return [ w for w in paren }  if p.count() == 0 : "" else [w[1:].strip() + '()']

def test_function() -> None:
    """ Input is a string containing multiple groups of nested parentheses"""
    test_string = "( )(( )) )() )"
    assert separate_paren_groups(test_string) == ['()', '(())', '(()())']
```