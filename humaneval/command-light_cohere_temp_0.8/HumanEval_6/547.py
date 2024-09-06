```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting for parentheses in the given string.
    Parameters:
    - The string to be parsed is a representation of multiple groups of parentheses separated by spaces.
    Returns:
    A list of integers, where each integer corresponds to the deepest level of nesting found.
    """
    Example test cases can the test cases, using the test case function to check the output of this function. 
"""
    test_cases = {
        ("()()", 1),
        ("()()()", 2),
        ("()()()()()()()", 3),
        ("(())()", 4),
        ("(())()()()()", 5),
        ("() ()", 6),
        ("() () ()", 6),
        ("() ()() ()", 6),
        ("()  ()()() ()", 6),
        ("()  (())() ()", 7),
        ("() () () () ()", 8),
        ("()() () ()() ()", 9),
        ("()() () () () () ()", 10),
        ("()()  () () () () ()", 10),
        ("()()()()()()()()()", 10),  # This is 10 levels deep
        }
    test_parent_string = "()"
    test_cases_results = [parse_nested_parens(test_parent_string),]
    assert test_cases_results == [1, 2, 3], "Failed to parse correctly."
```