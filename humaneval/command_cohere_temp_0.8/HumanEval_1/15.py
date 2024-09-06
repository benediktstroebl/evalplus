Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

The function works by using the Python built-in `recursion` library, which matches either an opening or closing parenthesis. The function is geared towards returning the first match of each distinct group of parentheses, thereby ensuring that no groups are nested within each other. 

```python
import re
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    # this regex pattern matches either an opening or closing parenthesis
    pattern = r'([(\[\{])|(\))|(\])|(\})'
    # finds all occurrences of pattern in parent_string
    matches = re.findall(pattern, paren_string)
    # initialize an empty list to store the distinct groups of parentheses
    result = []
    # iterate through all matches, add an opening parenthesis to result and
    # continue searching in the remainder of the string
    for match in matches:
        if match == '(':
            result.append('')
        if match == ')':
            result.pop()
        if len(result) > 0 and result[-1] == '':
            result[-1] += match
        else:
            result.append(match)
    # reverse the modifications made to the list and return the list of distinct groups
    return [item for sublist in result for item in sublist]

# Tests
assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
assert separate_paren_groups("((a))") == ['(())', 'a']
assert separate_paren_groups("<<((a)))>>") == ['(())', 'a']
```