```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Removes spaces, correctly separates parentheses and returns the list of strings.
    Args: 
    - s: the input string containing parentheses
    Returns:
    - List of strings, each representing a separate group of parentheses
    """
    return [p.replace(p.replace(' ', '') for p in s.replace(' ', '', '').split()) for p in s.replace('', '', '')]
``` 
The function does the following:
- Remove spaces 
- Split the string into individual groups using `split()` 
- Use a generator expression to replace each group with an empty string to remove spaces
- Call `p.replace()` to remove the spaces from each group. 
- Return the list of strings.