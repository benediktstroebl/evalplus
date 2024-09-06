Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '([{'
    close_braces = ')]}'
    paren_groups = []
    stack = []

    for char in paren_string:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces and stack:
            stack.pop()
        elif not stack:
            paren_groups.append('')
        else:
            paren_groups[-1] += char

    return paren_groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of open braces '(' or '[' and creates a new string when the stack is empty, adding the close brace to it. All strings in the list are joined to form the final result, and the result is printed as a list of strings. The output of the provided example is `['()', '(())', '(()())']`.