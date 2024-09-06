```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string with multiple groups of nested parentheses separated by spaces as input and returns the deepest level of nesting of parentheses.
    :param parent_string: The string containing groups of parentheses.
    :return: List of indices pointing to the deepest nested parentheses.
    """
    strings that contain multiple groups of parentheses and separated by spaces.

    Example the following steps to solve the problem:
    - Store the current index in a list.
    - Iterate through over the strings and push the current index.
    - Push the string while it starts with a group of parentheses, it should have the same level of nesting.
``` 
Now, let's test the function with a sample input:
```python
parse_nested_parens('(()()) ((())) () ((()))()')
 [2, 3, 1, 3]
```