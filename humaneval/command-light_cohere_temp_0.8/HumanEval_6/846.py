```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function splits a string of nested parentheses into a list of the deepest level of each group.
    Parameters: Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    Returns: A list of the deepest level of nesting for each group.

    >>> Examples:
        '(()()) ((())) () ((()))' => [2, 3, 1, 3]
        '((()))' => [0]
        """
    return [match.count(match.group()) for match in re.group for match in re.parse(*s)]
 [match.group() for match in re.parse(*s)]
 return [match.count(match.group()) for match in re.parse(*s)]
 test_parse_nested_parens("(()()) ((())) () ((()))())" == [2, 3, 1, 3])

test_parse_nested_parens("((()))'")
```