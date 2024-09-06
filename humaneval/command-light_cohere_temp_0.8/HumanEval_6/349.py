```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    # A list of numbers is returned as the result
    # The function returns [2, 3, 1, 3] 
    stack = []
    in_string = False  # Flag to track if in a closing parenthesis ')'
    for char in parentheses_string:
        if char == ')':
            if not_string:  # if not in a closing parenthesis, push the number into stack
                stack.append(int(in_string))
                in_string = False
            else:  # if in a closing parenthesis, reset the flag
                in_string = True
        elif char == '(':
            if in_string:  # if already in a closing parenthesis
                stack.append(int(in_string))
                in_string = False
            else:  # if not in a closing parenthesis, start a new group, and set the flag
                in_string = True
        stack.pop()
    finished = False
        for item in stack:
            if finished:  # check if all numbers are popped from stack
                break
            in_string = int(item)  # assign the number to in_string
        stack.append(in_string)  # push the current state of in_string to stack
    finished = True  # set finished to True to indicate the function has returned a full group
    return stack
```