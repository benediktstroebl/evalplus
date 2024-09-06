```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    """ This function parses a string represented multiple groups of nested parentheses separated by spaces. It returns a first level of nesting of parentheses.
    Args:
        parenthes_string (str): The input string containing nested parentheses.

    Returns: list of the deepest level of nesting of parentheses.
    Example:
        [('(()())',), ('()', '()', '()', '()', '()', 3), 1, 3]
    """
    return [Match for Match in map(lambda x: eval(x), parenthes_string.split())]

# Test the function
#Test cases
tests = [parse_nested_parens('(()()) ((())) () ((())()())'),
                   parse_nested_parens(')()()()((())())'),
                   parse_nested_parens('((()))'),
                   parse_nested_parens('(())()'),
                   parse_nested_parens(')())',
                   parse_nested_parens('()()())',
                   parse_nested_parens('()'))]

for test in tests:
    assert parse_nested_parens(test) == test
```