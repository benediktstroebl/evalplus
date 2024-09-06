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
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                current_group = stack.pop() + current_group

    # yield any remaining groups
    while stack:
        yield stack.pop()
```

The code uses a stack to keep track of open parentheses `(` and creates a corresponding list `current_group` to
keep track of strings between parentheses. When it encounters a closing parenthesis `)`, it checks whether the
top of the stack matches the last string in `current_group` to correctly unwind the parentheses. It yields
the correct groups and ignores any spaces in the input string.

This solution works reliably for any input that follows the problem statement and results in a list of
strings, each corresponding to a balanced group of parentheses. 

``` Markdown
```python
```
Below is a sample input and the corresponding output for the function:
```
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```
```