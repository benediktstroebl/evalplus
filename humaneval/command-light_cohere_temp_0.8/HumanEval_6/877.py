```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes in a string of nested parentheses separated by spaces.
    It returns a strings of corresponding depth of nesting.
    """
    input:
    ```
    string of parentheses separated by spaces
    ```
    return [i for i, char in enumerate(parent_string, 1) if char == "(".center())][::-1]  # reverse because it's a stack


def test_parse_nested_parens(test_string: str) -> None:
    """
    This function takes in a string of parentheses separated by spaces and checks whether the parse_nested_parens function returns the correct result.
    """
    test:
    ```
    Test string with correct nesting
    ((()))() ((())) () ((()))()
    should return [2, 3, 1, 3]
    """
    result = parse_nested_parens(test_string)
    if result != [2, 3, 1, 3]:
        raise Exception("Did not return expected result")
```