```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate each balanced group of parentheses into separate strings.
    :param s: input string containing parentheses
    :return: list of separated strings
    """
    return [p.split('()') for p in s.groups(list(s, 2)[::-1]]
```

This function uses list comprehension and the split() function to split the string at every second, open parenthesis. The groups of parentheses are balanced and each open brace is properly closed. The split() function returns each element as a separate string.