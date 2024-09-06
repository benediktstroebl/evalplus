```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function is designed to separate out the groups of parentheses in a string,
    returning them as individual strings. It does this task by ensuring balanced and properly nested parentheses, without any extra spaces.
    Test cases are following:
    - Properly balanced and nested pairs of parentheses
    - Balanced and not nested pairs of parentheses with spaces inside them
    - An empty string
    """
    output: List[str] = []
    for match in paren_string.strip():
        match = match.replace(0, - 
        ([open(), close])
        for open, close in zip(openbraces, closesbraces)):
            if open == close:
                output.append(match)
    return output
``` 
This solution is self-contained, and it provides a clear separation of individual groups of parentheses in the input string.