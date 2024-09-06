Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing only the separate groups of parentheses. The function works by using the concatenation (`*`) and slicing (`[i:j]) methods to extract the separate groups from the input string and uses open and closed parentheses (`'('` and `')'`) to determine the boundaries of each group.

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_stack = []
    open_parentheses = 0

    for i, char in enumerate(paren_string):
        if char == '(':
            open_parentheses += 1
            if not open_parentheses in paren_stack:
                paren_stack.append(open_parentheses)
        elif char == ')':
            open_parentheses -= 1

            if not open_parentheses == paren_stack[-1]:
                raise RuntimeError(f"Mismatched parenthesis at index {i}")

            if not open_parentheses == 0:
                # Pop until we hit the matching closing parenthesis
                while not open_parentheses == 0:
                    open_parentheses -= 1
                    paren_stack.pop()
            else:
                group = paren_string[paren_stack.pop()]
                if not paren_stack:
                    return [group]
                else:
                    return [paren_string[paren_stack[0]:paren_stack[-1] + 1]]

    return []

# Here are some example inputs for which the behavior should be the same as the example in the prompt:
example_inputs = [
    "()",
    "(())",
    "(()())",
    "( ) (( )) (( )( ))",
]

for input_ in example_inputs:
    print(f"Input: {input_}), Output: {separate_paren_groups(input_)}")
```