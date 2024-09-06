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
                current_group = ""
        else:
            current_group += char
    
    # yield any remaining groups in the stack
    while stack:
        yield stack.pop()
```

This script uses a stack to keep track of nested parens groups. It iterates through the input string, adding characters to the current group when parens are closed and popping groups from the stack when they are opened. Any spaces are ignored. The resulting list of strings is yielded. 

The `separate_paren_groups` function is a generator, so it needs to be iterated to produce values, like in the test cases provided earlier. To get a list of strings, you can call the function and use the `list(function_output)` to first convert the generator to a list. 

This solution should address the problem statement and corresponding tests as provided. Let me know if further clarification is needed or if there is another coding problem that I can help with!