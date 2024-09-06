```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    opening = False
    closing = False
    parentheses_count = 0
    output = []
    for char in parent_string:
        if char == "(":
            if opening == True:
                stack.append(parentheses_count)
            opening = False
            closing = True
        elif char == ")":
            if closing == True:
                output.append(parentheses_count)
                closing = False
            else:
                stack.append(parentheses_count)
                opening = True
                closing = False
                parentheses_count += 1
        else:
            stack.append(char)
    if closing == True:
        output.append(stack.pop())
        return output
return output
```
This function is able to parse and organize a string of nested parentheses. It works by maintaining two flags, `opening` and `closing`, which indicate whether we are in an `opening` or `closing` state. The `parentheses_count` keeps track of the number of parenthesis encountered. The function uses a stack data structure to organize the `parentheses_count` as we move through the string. The function returns a list containing the deepest level of nesting for each group of parenthesis encountered.