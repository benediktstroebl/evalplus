```python
from typing import List

def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate each group of parentheses into individual strings.
    Return a balanced (each open brace is properly closed), non-nested, and spaces are preserved.
    """:
    return [parentheses.split('()')]
```

This script defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, where each string represents a balanced and properly-formed group of parentheses.  The use of the split() method to split the string into individual characters.