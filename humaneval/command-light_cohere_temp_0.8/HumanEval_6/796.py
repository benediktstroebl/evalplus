```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            else:
                output.append(parse_tree_substructure(stack) [::-1]))
            stack.append(0)
    return output
```

The code takes a string of nested parentheses and returns a list of the deepest level of nesting.