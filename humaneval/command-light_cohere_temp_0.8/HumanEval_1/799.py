```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Separate and rearrange the list of parentheses into a properly formatted string.

    :' Help not to break the parentheses beyond the first or last character
    """
    def char_to_close(c):
        return ')' if c == ')' else '('
    return ''.join(char_to_close(c) for c in parentheses)
```