```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of parentheses into separate strings.
    """
    strings = []
    for match in s.match("(\S)+?", s):
        strings.append(match.group())
    strings
    more than one group of parentheses.
    return strings
more than one group of parentheses, return an empty list.
    """
    ``` Group of parentheses contains balanced parentheses and should be returned as a single string.