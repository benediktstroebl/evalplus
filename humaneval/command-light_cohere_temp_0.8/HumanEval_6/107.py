```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes in a string of multiple groups separated by spaces, representing nested parentheses. 
    Returns a value is a list of the deepest level of nesting of parentheses.
    """
    deepest level is represented as the order of the group.

def test_parse_nested_parens(input_str: str, expected_output: List[int]) -> None:
    """
    This function tests the parse_nested_parens function with a given string of input and an expected output. 
    Args: 
        - input_str: the input string to test.
        - expected_output: the expected output of the parse_nested_parens function
    """
    assert parse_nested_parens(input_str) == expected_output, "Input string does not return the expected output."
def main():
    test_parse_nested_parens("(()()) ((())) () ((()))", [2, 3, 1, 3])
    test_parse_nested_parens("((())) () ((()))", [1, 3])
    test_parse_nested_parens("( ))()()()()()()()()()", [2, 3, 1])
if __name__ == "__main__":
    main()
```