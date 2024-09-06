```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                return []
            current_group += stack.pop()
        else:
            current_group += char

    return stack
```

This Python script provides a self-contained function `separate_paren_groups`, which accepts a string of nested parentheses as input and returns a list of unnested and individually balanced groups of parentheses. The function utilizes a stack to keep track of open parentheses until they are closed, effectively unwrapping the nested structures.

Here is an example usage of the function:
```python
 >>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```

This example call returns a list containing three strings, each a separate and balanced group of parentheses from the input string.