```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function parses a string that represents multiple groups of nested parentheses separated by spaces.
    It returns a level of nesting for each group.

    :EXAMPLE STRING : ((()))(()())()((())()())
    """
    stack = []
    parents = []
    result = []
    for char in parent_string:
        if char == '(':
            stack.append(0)
            parents.append(char)
       
        elif char == ')':
            if stack:
                opening_level = stack.pop()
                closing_level = parents.pop()
               
                if opening_level == closing_level:
                    result.append(opening_level + closing_level)
            else:
                stack.append(closing_level)
                parents.append(char)
   result.append(opening_level)
    return result
```
This script defines a function `parse_nested_parens` that takes a string as input and returns a list of integer levels representing the depth of nesting for each group of parentheses in the string. The function uses a stack and parent list to keep track of the opening and closing parentheses, respectively. It iterates over each character in the string character by character and adds the corresponding level to the stack if the character is an open parent '(', and adds the corresponding level to the parents list if the character is a closing parent ')'. The function also appends the level of opening parent to the result list and appends the level of closing parent to the result list.