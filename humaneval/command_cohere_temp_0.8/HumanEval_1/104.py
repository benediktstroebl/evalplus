Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

The function works by using the `reversed` function to iterate through the input string from the end to the beginning. By doing this, the function can detect when a closing parenthesis is encountered, thus incrementing the `depth` variable when an opening parenthesis is encountered, and decrementing it when a closing parenthesis is encountered. When the depth variable is zero at the end of a loop iteration, this indicates that a group of parentheses is closed, and the group is then added to a list which is returned at the end. 

Note that the code assumes that the input string contains only parentheses and no other characters. You can add additional checks or sanitization procedures to handle additional scenarios or edge cases. 

```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    closed_groups = []
    depth = 0
    for i in range(len(paren_string)-1, -1, -1):
        if paren_string[i] == '(':
            depth += 1
        elif paren_string[i] == ')':
            depth -= 1
            if depth == 0:
                closed_groups.append(paren_string[::-1][i+1:i-depth])
    return closed_groups

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```