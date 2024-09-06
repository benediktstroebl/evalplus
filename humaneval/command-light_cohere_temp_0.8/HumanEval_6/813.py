```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function aims to parse and return the deepest level of nesting of parentheses from the provided string.

    Parentheses are return as an list of their levels. 
    """

    example: ['(())', '(()())', '()()()']

    Each level represents a nested group of parentheses, with the innermost group having level 1 and the next level being outermost groups. 

    way to represent the nested groups of parentheses. 

    way to represent nested groups of parentheses.

Example:
```python
test_parse_nested_parens("((())) () ((()))")")
[(3, 2, 1)]
test_parse_nested_parens("(((()()))) ")")
[(3, 1)]
test_parse_nested_parens("(()()) ((()))")
[(2, 3, 1)]
```