```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate groups of balanced parentheses into individual strings.
    Returns a individual string for each group of balanced parentheses.
    """
    balanced group is returned as it is without any spaces.
    """
    test_case = """
    Input: ( ) (( )) (( ) ) )

    Output: ('(', ')')
    """
    return [ parentheses for parentheses in parentheses.group if ')' in parentheses. imbalance else parentheses.

parentheses = "() (( ) ())"
formatted_output = separate_paren_groups(parentheses)
print(formatted_output)
``` 
This script defines a function named `separate_paren_groups` that takes a string of parentheses as input and returns a list of individual strings created by separating balanced groups of parentheses.