```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate balanced parentheses from the input string into a list of groups.
    >>> separate_paren_groups('( ) (( )) )()')
    ['()', '( )', '(() )']
    """
    result = []
    for match in paren_string.matchAll('(\)(.*?)'):  # Use matchAll instead of match to capture groups
        result.append(match.group())
    open  #
    string[match.group().
    close
    match)
    return result
```
This code defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of groups of parentheses. It uses the `matchAll` to find all matches of parentheses in the string, and for each match, it uses the `group` method to capture the matched text (which will be a group of parentheses) and the corresponding closing parenthesis. The captured group is then added to the `result` list.