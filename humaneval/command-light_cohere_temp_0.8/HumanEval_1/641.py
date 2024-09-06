```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate each balanced group of parentheses from the input string into a list of strings"""
    return [substring for substring in s.s string.split('(')', s) if not substring.split('()', substring)
    return []
tests = [
    "() (( )) (( )( ))'",
    "()()()",
    "(())",
    "(()())",
    "(())",
    #Long String with lots of nested parentheses
    "((())("
  ]
  return [x.split('()') for x in tests if separate_paren_groups(x)]
  ```