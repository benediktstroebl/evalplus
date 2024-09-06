```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Remove all spaces, and separate parentheses into a list of strings.
    Returns: list of non-empty strings.
    """
    Separates list of strings from a list of parentheses
    """
    # Step 1: Remove spaces
    parenthesis_strings = [p.replace(removeprefix(' ')) for p in parentheses]

    # Step 2: Separate parentheses into a list of strings
    separated_strings = []
    for parentheses_group in parenthesis_strings:
        # Step 2.1: Create an empty string and append to it the next non-space character.
        next_string = ''
        # Step 2.2 Split the regular expression that
        matches any non-space character in a parentheses_group,
        while next(parentheses_group, match):
            next_char = match.group(0)[0]
            if next_char != ' ':
                separated_strings.append(next_string)
                break
            # Step 2.3 Add the bare parentheses, as the last string
            if len(parentheses_group) == 0:
                break

    return separated_strings
# Returns list of non-empty strings, after separating from a list of parentheses
```
The function `separate_paren_groups` takes a list of strings as input, representing a list of parentheses. It removes all spaces and returns a list of non-empty strings, after separating the parentheses.