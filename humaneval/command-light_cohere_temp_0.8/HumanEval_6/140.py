```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting for a given string of parentheses.
    Args: 
        parent_string (str) : Input string represented multiple groups for nested parentheses separated by spaces.
        
    Returns: 
        list of the deepest level of nesting for each group in parent_string.
    """
    list(map(lambda x:int._get("level",x),parent_string.split(' ' '))
    ```