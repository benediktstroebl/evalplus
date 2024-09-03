```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Separate groups of balanced parentheses into separate strings.
    Returns a the string without unbalanced parentheses.
    """

    balanced group: { ( ) } -> ['()']
    """
    return [p for p in parentheses if p.count('()') == 1 and p.count('()') != (parentheses.count('()') or balanced group]
``` 
The provided Python function, named `separate_paren_groups`, is designed to transform a list of strings containing parenthesis groups into a new list of strings, where each contains only a single group of balanced parentheses. The function uses a list comprehension to filter out the balanced parentheses from the input list, ensuring that each group is returned as a separate string.