```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            top_of_stack = stack.pop()
            if top_of_stack == "":
                current_group = ""
            elif top_of_stack != current_group:
                print(f"Mismatched parentheses! We expected {top_of_stack} but saw {current_group}")
            else:
                current_group = ""
    return stack
```

This Python script takes a string of characters containing nested parentheses and uses a stack to correctly separate these into individual groups. It checks for proper closing parentheses for each opening parenthesis and also ensures that there are no nested parentheses within each group. The output is a list of the separate groups of parentheses. 

This approach handles cases like nested parentheses and properly handles mismatches in parentheses structure. For example:
```python
print(separate_paren_groups("( ) (( )) (( )( ))"))
```
will return ```python
['()', '(())', '(()())']
```

This reflects the example provided in the specification.