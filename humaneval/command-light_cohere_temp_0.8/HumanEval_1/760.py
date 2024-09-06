```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates balanced parentheses groups into individual strings.

    >>>
    groups = separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    results = []
    for match in s.match('([ ]+)$:
        content = match.group().content()
        all content and trailing ')' is added to results.
    results.close_balanced_ -oo(), and return results
    """

This script defines a `separate_paren_groups` function that takes a string of parentheses (`())`) and returns a list of individual strings created by separating the groups of parentheses. The function uses the match() function with the regular expression `[ ]+$ to find each group of parentheses and returns the content of the group as a string.