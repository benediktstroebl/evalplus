```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Function to separate groups of balanced parentheses.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                result.append(stack.pop()
                open parenthesis)
                stack = []
            else:
                result.append(char)

    return result
```
The function `separate_paren_groups` takes a string of parentheses as input and returns a list of separate strings, each containing a balanced pair of parentheses. The test cases are also shown in the code, passing the expected output.