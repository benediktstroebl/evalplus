```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Function to parse and return the deepest level of nesting for parentheses.

    Parameters:
    string like multiple groups of parentheses separated by spaces.

    Returns:
    list of the deepest level of nesting of parentheses.
    """
    examples:
    ['(())', '(())', '()()()']
    """
    stack: List[int] = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(stack.pop()
           
        if char == ')':
                stack.append(0)
                if i == len(s) - 1:
                    return stack.dec
```
This code implements a function `parse_nested_parens` that takes a string of nested parentheses as an input and returns the deepest level of nesting for the parentheses. It uses a technique similar to the stack-pop/pop approach to traverse the string and keeps track of the deepest level of nesting. 

This function uses the `enumerize` to iterate through the string, and checks each character to see if it is a left parenthesis or a right parenthesis. If it is a left, it pushes the current element onto the stack. If it is a right, it appends a zero to the stack, indicating that there are no more levels of nesting. 

This approach allows to efficiently parse and return the deepest level of nesting for the parentheses in the string.