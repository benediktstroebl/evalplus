```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    Returns the deepest level of nesting for parentheses in the string.
    Args:
        parent_string (str): The input string to parse for nested parentheses.
    Returns:
    list of int: A list of the deepest level of nesting for each group of parentheses.
    """
    test:
    test_case = "(()()) ((())) () ((())()())"
    test_output = parse_nested_parens(test_case)
    assert test_output == [2, 3, 1, 3]

Example usage:
    parsed_output = parse_nested_parens("(()()) ((())) () ((()))")")
    print(parsed_output)
    ```