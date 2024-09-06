```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns each group of parentheses in a string.
    Groups should be balanced (each open brace is properly closed)
    Returns list of strings, each containing a balanced group of parentheses.
    """
    list()
    # to keep the original list of strings
    """
    return [brace.join() for brace in s if brace.is_balanced_open()]
```

This function uses a list comprehension to iterate over each balanced open brace `brace` in the input string `s`. It uses the `join` method to join the elements of the list into a single string. The resulting string contains a balanced group of parentheses and the function returns a list of these strings.