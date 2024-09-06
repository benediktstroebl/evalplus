```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string with multiple groups of nested parentheses separated by spaces as input and returns the deepest level of nesting of parentheses.
    Return list will the specific order of nested parentheses: [level] -> [left_bracket, ... items, right_bracket]
    """
    brackets = []
    stack = []
    for char in parent_string:
        if char == ')':
            if stack:
                brackets.append(stack.pop())
                continue:
                    stack.append(')
            continue:
                stack.push(')')
        else:
                    stack.push(char)
        continue
        elif char == '(':
            stack.append(char)
    continue
    return brackets
```
The given code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting parentheses found. The function uses a stack data structure to keep track of the open parentheses encountered. 

The code uses a for loop to iterate over each character in the input string. 

For each character, it checks if it's a closing parenthesis `(`) and if there's an open parenthesis `(`), it adds the closing parenthesis to the stack. If the character is an open parenthesis `(`, it adds it to the stack. 

Finally, the function returns the brackets in the stack, which represents the deepest level of nesting parentheses found in the input string.