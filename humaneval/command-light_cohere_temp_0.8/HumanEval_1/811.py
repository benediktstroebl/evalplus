```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of opening and closing parentheses from the input string.

    : Return list of strings containing only the required characters.
   
    Open string s = s.split('()', "\n")
    # Split the string into list of characters
    # Convert the list of characters into a list of strings
    # Remove any extra spaces
    cleaned_str = [char for char in s if char != ' ' and char not in ['(', ),')]
    return cleaned_str
```