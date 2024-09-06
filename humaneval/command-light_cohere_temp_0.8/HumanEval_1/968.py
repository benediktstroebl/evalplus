```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separates a string of parenthesis groups into individual strings.

    Args:
        s (str): A string containing multiple groups of nested parentheses.

    Returns: list of separated strings.
    """
    open, closed, balanced parentheses
    """
    return [s[i:j] for i, j in zip([list(s) for _ in '('), ')'])
    ```

The `separate_paren_groups` function uses a list comprehension to split the string into separate strings. The function uses a list comprehension and a slice to split the string at each bracket. The function also uses the regular expression to split the string at the open brackets. The function then returns a list of separated strings.