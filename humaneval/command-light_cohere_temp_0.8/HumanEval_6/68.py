Here is a self-contained Python script with a function that solves the problem of finding the deepest level of nesting for multiple groups of parentheses:
```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function returns a list of deepest level of nesting for each group of parentheses in the string.
    Args:
    parenthesis_string (str): The string to be checked for nested parentheses

    Returns:
    List[int]: A list of integers, with each integer representing the deepest level of nesting of a parenthesis group.
    """
    raising an exception to a list
    """
    nesting_levels = []
    for group in parentheses_string.group():
        if len(group) > 0:
        nesting_levels.append(len(group))
    return nesting_levels

def test_parse_nested_parens(parentheses_string: str) -> None:
    """
    Test function to verify the parse_nested_parens function.
    Args:
    parenthesis_string (str): The input string to test
    """
    result = parse_nested_parens(parentheses_string)
    assert len(result) == len(parentheses_string), "Nested parentheses found"
```
This Python script defines a function `parse_nested_parens` that takes a string of parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses in the string. The function iterates over each group of parentheses in the string and uses the `len` function to check if the group is empty. The function then raises an `ValueError` exception if the group is not empty. The `test_parse_nested_parens` function takes a string of parentheses as input and calls the `parse_nested_parens` function to get the result, and then asserts that the length of the result is equal to the length of the input string.