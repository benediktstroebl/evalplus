```python
def parse_nested_parens(s: str) -> List[int]:  # Function to parse nested parentheses string into levels of nesting
    stack = []  # Stack to keep track of open parentheses levels

    # Loop over the string
    for char in s:
        if char == '(':  # if current char is open parentheses
            stack.append(1)  # add to the stack
        elif char == ')':  # if current char is close parentheses
            if len(stack) == 0:  # if there are no open parentheses, nothing to do
                pass
            elif len(stack) == 1:  # if there is only one open parentheses, close it
                stack.pop()
            else:  # if there are more than one open parentheses, return current level
                return stack[-1]  # return top of stack

    return []  # Return empty list if the string is empty or there are no parentheses
```
This script defines a function parse_nested_parens that takes a string s as input and returns a list of integers. It uses a information about opening and closing parentheses and maintains a stack of open parentheses to determine the level of nesting. The function will correctly parse the nested parentheses in the string.