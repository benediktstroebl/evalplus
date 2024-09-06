```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Function to separate and return list of non- nested parenthesis groups.

    : Parameters
   :
    parenthesis_list: list of strings containing parenthesis groups.

    Returns: list of strings, with each one being a non-nested parenthesis group.
    """
This function uses a list comprehension to split the input list of strings into a list of strings, where each string is a non-nested parenthesis group.
    """ 
test cases:
    1. Test with empty list.
    2. Test that empty list is doesn returned [] and not modified
    3. Test with a list of strings containing only one set of parenthesis
    4. Test with list of strings containing multiple sets of parenthesis.
    5. Test that the valid function on a list of strings with unbalanced (unclosed) parenthesis
    6. Test with list of strings with nested parenthesis.
    """ 
example output:
    ['())', '()()()']
```