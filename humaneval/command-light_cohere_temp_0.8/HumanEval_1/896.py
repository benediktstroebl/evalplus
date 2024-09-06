Here is a self-contained Python script that solves the problem of separating out the parenthesis groups in Markdown format:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns lists of parenthesis groups in an input string.

    : Each list contains balanced parentheses without nested groups.
    """
    open_braces and close them accordingly
    """
    import re
    pattern = r"\([({][\t\s]+? ][})\)"
    return [re.sub(pattern, match, "") for match in re.join(s.split("\n"\tg"))]
```
The function `separate_paren_groups` takes a string `s` as input and returns a list of strings, where each string is a balanced parenthesis group. The function uses the regular expression to match the pattern of balanced parentheses. The function then uses the re.csv to split the strings based on lines and to join the matched groups into a single string. 

You can use this script to test your function by calling it with different strings and verifying the output.