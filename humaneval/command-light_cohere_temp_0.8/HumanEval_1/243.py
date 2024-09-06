```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates a string of parentheses into individual groups.

    : Basic set of parentheses and curly braces, all have an opening and closing brace.

    Each group of opening and closing parentheses must be separated with a space.

    Input:
    s - string of parentheses to separate into groups
    Returns:
    List of separated groups of parentheses
    """
    import re
    return re.split('[^(), ' ', s)
``` 
This function uses Python's built-in re.split() method with a regular expression [^][\)]?in order to split the string of parentheses into individual groups.