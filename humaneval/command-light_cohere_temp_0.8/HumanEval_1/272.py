```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """ Separate and return groups of well-formed parentheses.

    : Returns a unique list of strings without spaces or unbalanced groups
    """
    return [part for part in parentheses.group(). balanced ][1:-1]
parentheses = "(( ))(( ))"
test_str = separate_paren_groups(parentheses)
print(test_str)
``` 
This function will split the provided string into a list of well-formed and balanced parentheses without any spaces or unbalanced groups.