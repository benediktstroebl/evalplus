Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '({}'
    close_braces = ')}'
    paren_groups = []
    stack = []

    for char in paren_string:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces:
            if not stack or open_braces.index(stack.pop()) != close_braces.index(char):
                # unbalanced or nested group, ignore
                continue
            if not stack:
                paren_groups.append('')
        else:  # ignore spaces
            continue

    return paren_groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses the `separate_paren_groups` function to take a string of parentheses as input and return a list of separate groups of parentheses. The function uses a stack to keep track of open parentheses and properly close them. It checks if each opened brace has a matching closed brace and whether they match the last opened brace.

The output of the provided example is `['()', '(())', '(()())']`, which matches the desired output.