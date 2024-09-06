Here's the corrected self-contained Python script:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function returns the deepest level of nesting of parentheses in the input string.

    Parentheses are nested, like (()) with more than 3 levels of nesting, will return an error message.

    Parameters:
    Input string containing groups of parentheses separated by spaces.

    Returns: Error messages if the input string doesn't match the expected format.

    Returns: List of integer levels of nesting of parentheses.
    """
Deepest level of nesting is a List of integer values.
    """

Example usage:
    >>> parse_nested_parens('(()()) ((())) () ((()))')
    [2, 3, 1, 3]
    """
    groups = s.split('() + ' ')
    groups = [group.strip() for group in groups]

    nesting = {}
    for i, group in enumerate(groups):
        nesting[group] = []

    stack = []
    for group in groups:
        nesting[group].append(stack.append(1))

    nested = []
    for i, nesting_level in enumerate(nesting):
        if nesting_level > 3:
            print(f"Warning: Ignoring nesting level {nesting_level} with {nesting}")
        nested.append(nesting_level)

    return nested
```
The code splits the input string into groups of parentheses, and then iterates over each group. It uses a nested lists to keep track of the deepest level of nesting, and returns the list of integer values representing the deepest level of nesting.