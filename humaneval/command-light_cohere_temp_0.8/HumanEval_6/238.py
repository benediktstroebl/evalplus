```python
from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function takes a string with multiple groups of nested parentheses separated by spaces as input and returns a list of deepest nesting levels.

    The most basic group is ((())) and the function uses parentheses grouping to traverse over the string and returns a list of the deepest nesting levels of parentheses found.
    """
    strings with different grouping, such as (()) and ((())) are treated the same way.
    """
    List of deepest nesting levels of parentheses found.

def test_parse_nested_parens():
    """ Test function to check the correctness of the parse_nested_parens function
    """
    test_str = "(()()) ((())) () ((())()())"
    result = parse_nested_parens(test_str)
    expected = [2, 3, 1, 3]
    assert result == expected
    test_str = "((())) ((()))"
    result = parse_nested_parens(test_str)
    expected = [1, 3]
    assert result == expected
    test_str = "((())) ()()"
    result = parse_nested_parens(test_str)
    expected = [1]
    assert result == expected

 ```

The test_parse_nested_parens function provides a basic test suite to check the correctness of the `parse_nested_parens` function. 
It creates test strings with different grouping and nesting levels, calls the `parse_nested_parens` function, and asserts that the result matches the expected output. 

This test suite can be extended with more test cases to cover various scenarios and ensure the function's correctness.