```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Function to separate groups of nested parentheses.
    : Returns a for each group in the string, it will look for the matching opening parenthesis 
    : If found, the function will split the current group from the remaining part of the string and 
    : return the split group.

    : continue this the example, we will continue splitting until no matching opening 
    parentheses found.

    : Each split group will be without any leading or trailing spaces, thanks to the 
    : "keep spaces" rule.
    """
    expected output:  ['()', '((()))', '(()())']
    """
    return [s[i:i+3] for i in range(0, len(s), 3)]
```