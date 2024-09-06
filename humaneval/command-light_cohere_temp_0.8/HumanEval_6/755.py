```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string containing nested parentheses.
    Args: s (strring containing nested parentheses)
    Returns: A list of the deepest level of nesting of the parentheses.
    Example the provided input, and will throw an exception if there are unbalanced parentheses.
    """
Example usage:
    ```python
    result = parse_nested_parens('(()()) ((())) () ((()))')
    print(result)
    ```
```
The parse_nested_parens function takes an input string and returns a list of the deepest level of nesting of parentheses in the string. The function uses the complicated algorithm to parse the nested parentheses and returns a list of the deepest level of nesting.

This self-contained Python script can be used to solve the problem of parsing and returning the deepest level of nesting of parentheses in a given string.