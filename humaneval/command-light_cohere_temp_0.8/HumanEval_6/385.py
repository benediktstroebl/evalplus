```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with nested parentheses into a list of their depths.

    Parameters:
    s: str
        The string with nested parentheses.

    Returns:
    List[int]: list of depths of each group of parentheses in order of appearance.
    """
    nested parentheses are separated by spaces, and the function ignores other spaces.
    """
    string should not be empty.
    """ Returns a  depth of 3 for each group of parentheses, in order of appearance.
    """
    nested parentheses can be: ()(), (()), (()), ()(), ((()))
    """
    depths = []
    for i in range(len(s)):
        if s[i] == '(':
            depths.append(0)
        elif s[i] == ')':
            depths[-1] += 1
        else:
            depths.append(None)
    return depths
```
This function takes a string s as input and returns a list depths containing the depth of each group of parentheses in the string. The depths list is filled by 0 for the open parentheses and 1 for closed parentheses. The function ignores spaces and other characters. The function returns a expected output.