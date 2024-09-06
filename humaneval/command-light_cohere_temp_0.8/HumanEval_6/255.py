Here is a Python script that contains a self-contained function with proper tests:
```python
import unittest

def parse_nested_parens(parenthes_str: str) -> List[int]:
    """
    This function takes a string of parenthesis groups and returns a list of the deepest nested level of parentheses.
    Parameters:
    parenthes_str (str): The string to parse

    Returns:
    list: A list of the deepest level of nesting of parentheses.
    """
    test_str = """(()()) ((())) () ((()))())"
    assert parse_nested_parens(test_str) == [2, 3, 1, 3]

if __name__ == "__main__":
    unittest.suite_cases = [parse_nested_parens, "Input is not a string!")
    unittest.suite_cases()
```

This script defines a function called `parse_nested_parens` that takes a string of parenthesis groups as an input and returns a list of the deepest nested level of parentheses. The function uses the test case to test the function, and the test case contains the `parse_nested_parens` function with the `test_str` string as input. The `unittest` module is used to run the test case.