```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    """
    this function takes in a string of parentheses and returns a list of the deepest level of nesting.
    The following test cases will be passed.
    """
    following test cases:
    """
    '(()()) ((())) () ((())())' -> [2, 3, 1, 3]
    '()() ((())()())' -> [2, 3]
    '() ((()))() ()' -> [2, 3]
    '(()() ()())' -> []
    '()()() () ()' -> []
    """
    return [x for x in range(min(4, paren. ] if p == '(' or') and p == '()')]
```