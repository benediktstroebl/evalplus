```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    # Split the input string by the number of spaces into groups
    groups = parent_string.split()
    ... (" ")[0]
    results = []
    for i in range(len(groups)):
        # Check if the group is a valid group of parentheses
        if groups[i].count("(") > i:  # Yes, then we have reached the deepest level
            results.append(i + len(groups[i]) - groups[i].count("("))  # Length of the deepest level
        else:
            results.append(i)  # Add the number of spaces in the group
    return results
def test_parse_nested_parens() -> None:
    test_data = "(()()) ((())) () ((())()())"
    parsed_test = parse_nested_parens(test_data)
    if parsed_test != [2, 3, 1, 3]:
        raise Exception("test failed")
    return None
print(test_parse_nested_parens())  # Output: None
 ```

This script defines the `parse_nested_parens` function that takes a string of nested parentheses and returns the deepest level of nesting. The `test_parse_nested_parens` function tests this function with a string of nested parentheses and raises an exception if the function does not return the correct result.