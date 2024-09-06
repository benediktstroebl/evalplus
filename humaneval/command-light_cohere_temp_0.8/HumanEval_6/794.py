```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for char in parentheses_string:
        if char == '(':  # Push opening parenthesis onto stack
            stack.push(1)
        continue
        if char == ')':  # Pop closing parenthesis
            pop = stack.pop()
            if pop == 1:
                result.push(0)
            continue
        elif pop != 0:
            stack.append(pop)
    continue
    return result
``` 
This function takes a string of nested parentheses and returns a list of the deepest level of nesting for each group. It uses a stack data structure to keep track of opening parentheses and their corresponding depths. It processes the string character by character, updating the stack and result list accordingly.