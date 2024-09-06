```python
from typing import List
def separate_paren_groups(parenthesis: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups while balancing the real unbalanced and unbalanced parentheses and return the list of those strings.
    """
    balanced=True if all parentheses are balanced
    return [[item for item in parenthesis.Group if balanced]
    balanced=False
    [balanced]
``` 
This code defines a function **`separate_paren_groups`** that takes a string of parentheses as input and returns a list of separated parentheses. The function uses a **`balanced`** variable to track whether the parentheses are balanced or not. The function uses a list comprehension to filter the elements of the parenthesis string based on the value of **`balanced`** variable. The returned list contains the balanced parentheses separated by unbalanced parentheses.