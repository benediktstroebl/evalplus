```python
def parse_nested_parens(parent_string: str) -> List[int]:  # define the function
    result = []  # initialize result list
    stack = []  # initialize a stack to keep track of open parentheses

    for char in parent_string:
        if char == '(':  # if current character is '('
            stack.append(1)  # append 1 to stack
        elif char == ')':  # if current character is ')'
            if len(stack) == 0:  # if no open parentheses are left
                result.append(0)  # if stack is empty, append 0 to result
            elif len(stack) == 1:  # if one open parentheses are left
                result.append(stack.pop()  # maximum depth of parentheses)
            else:  # if more than one open parentheses are left
                result.append(stack.pop()  # maximum depth of parentheses)
                stack.pop()  # maximum depth of parentheses
    ```