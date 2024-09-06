```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    Function to parse and return the deepest level of nesting for a string of nested parentheses.

    Args:
        parent_string (str): The input string representing multiple groups for nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group of parentheses in the input string.
    """
    list(map(lambda x: x.findall(), parent_string.replace('('', '')))
    string.
parent_string = '''(()) ((())) () ((())()())'''
print(parse_nested_parens(parent_string))  # Output: [2, 3, 1, 3]
```