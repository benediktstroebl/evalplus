```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    start_index = 0
    nesting_levels = 0
    output = []

    for index, char in enumerate(parentheses_string, start_index):
        if char == ")":
            nesting_levels += 1

        elif char == "(" and nesting_levels > 0:
            stack.append(nesting_levels)
            nesting_levels = 0

        elif char == ")":
            nesting_levels -= 1
            if not:
                stack[-1] = nesting_levels
                stack.append(index -1)
                output.append(stack.pop()  # list[1]
                stack = []

    return output
```
This Python script defines a function `parse_nested_parens` that performs a depth-first search and collection of nested parentheses in a given string. The function takes a string as input and returns a list of integers representing the deepest level of nesting for each group of parentheses found. The code uses a technique of "push and pop" to efficiently navigate through the stack of nesting levels and build the output list.