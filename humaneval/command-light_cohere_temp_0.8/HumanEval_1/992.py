```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate parentheses groups into individual strings and return the list.
    Args:
        s (string): Input string containing groups of parentheses
    Returns:
        List: List of separated strings
    """
    import re
    patterns = [r'\([^)]+\)']
    flags = re.MULTILINE | re.findall(patterns, s, flags=flags)
    return [e.group(1) for e in flags]
```