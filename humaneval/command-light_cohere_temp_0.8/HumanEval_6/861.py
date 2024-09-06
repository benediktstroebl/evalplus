```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    """
    This function returns the deepest level of nesting of parentheses in the input string.
    Args:
        parenthes_string (str) : The input string is expected to contain multiple groups of parentheses separated by spaces.
    Returns:
    list of integers.
    """
    deepest level of nesting in the string
    """
    parentheses = []
    for i in range(len(parenthes_string)):
        opening, closing = parenthes_string[i], ')' + parenthes_string[i + 1]
        if opening == closing:
            parentheses.append(i)
   
    return parentheses
```