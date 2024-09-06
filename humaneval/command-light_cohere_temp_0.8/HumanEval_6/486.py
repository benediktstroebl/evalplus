```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    for char in parent_string:
        if char == " ": stack.append(0)
        if char == ")": stack.pop()
        empty_level = stack.append(0)
        if not empty_level:
            if char == "(": empty_level += 1
            stack.append(1)
            elif char == ")": empty_level -= 1
            stack.pop()
            if char != " ": result.append(empty_level)
    return result
``` 
This script defines a function called `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the empty levels of nesting. The function works by using a stack data structure to keep track of the opening and closing of parentheses. 

This function can be used to parse any string of nested parentheses and returns the list of empty levels of nesting.