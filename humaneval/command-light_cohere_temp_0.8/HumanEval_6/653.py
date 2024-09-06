```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function splits a string with multiple groups of nested parentheses into a list of their deepest nesting level.

    : Input is a string of multiple groups of parentheses separated by spaces.

    Returns a result of this function is a list of the deepest level of nesting in parentheses.

    Test case:
    Test string with valid nested parentheses
    """
    list_result = []
    for group in s.group(()) :  # Add each group to the list
        list_result.append(group.count_leading_open(group))
    return list_result

# Test cases
test_cases = [
    ("(()())((()))()()),",
    ("()()())((()())()))",
    ("()()()()())()()()()()()()()()",
    # Add more test cases here...
]

# Test function
def test_parse_nested_parens() :
    """
    Test function to check if the parse_nested_parens function works correctly
    """
    for s in test_cases :
        resulting_levels = parse_nested_parens(s)
        expected_levels = [2, 3, 1, 3]  # Desired output
        assert resulting_levels == expected_levels,
        print(f"Test passed for {s}")

if __name__ == "__main__":
    test_parse_nested_parens()  # Run the test when the script is executed
```
This Python script defines a function called `parse_nested_parens` that splits a string containing multiple groups of parentheses into a list of the deepest level of nesting. It then provides a test cases to verify the function's correctness. The test function checks if the resulting list of deepest levels of nesting matches the expected output for each test case. If the two lists are equal, the test passes.