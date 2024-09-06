Here's the self-contained Python function:
```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function is designed to parse a string of nested parentheses and return the deepest level of nesting.

    Args:
        s (string): Input string containing multiple groups of parentheses separated by spaces.

    Returns:
    list of the deepest level of nesting in the string.
    """
    # Use the format of parentheses:  }()())()()
    """
    # Define a recursive function to split string by spaces and return the elements of nested parentheses
    def recursive_split(element: str) -> List[str]:
        return [element] if not element else [element[0]] + recursive_split(element[1:])

    # Use list comprehension to build a list of nested parentheses
    parenth_list = recursive_split(s)

    # Return the deepest level of nesting
    return [len(p) for p in parenth_list if p and len(p) > 1]
```
This function takes a string as an input and returns a list of the deepest level of nesting in the string. 

It uses a recursive splitting approach to handle the nested parentheses and returns the appropriate output.