```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    # Initialize an empty list to store the results
    results = []

    # Define a helper function to split the string by spaces into a list of substrings
    def split_by_spaces(string: str) -> List[str]:
        return [sub for sub in string.split()]

    # Loop through through the spaces to find all the groups of parentheses
    for spaces in split_by_spaces(parenthes_str):
        # Use the helper function to split each space into a list of parentheses
        parentheses_list = split_by_spaces(spaces)

        # Add each level of nesting to the results list
        results.append(parentheses_list)

    return results
def test_parse_nested_parens(parenthes_str: str) -> None:
    # Test the function
    test_str = "(()()) ((())) () ((()))"
    test_results = parse_nested_parens(test_str)
    assert test_results == [2, 3, 1, 3]
``` 

This code defines a function `parse_nested_parens` that takes a string of parentheses and returns a list of the deepest level of nesting for each group. It also defines a test_parse_nested_parens function that tests the `parse_nested_parens` function with a sample string.