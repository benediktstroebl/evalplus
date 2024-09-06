Here's a self-contained Python function that solves the problem of finding the deepest level of nesting of parentheses in a given string:
```python
def parse_nested_parens(parenthesis_string: str) -> List[int]:
    stack = []
    in_string = False  # To track if we are inside an open parenthesis
    result = []  # List to store the deepest level of nesting

    for char in parenthesis_string:
        if char == "(":
            if not in_string:
                stack.append(1)  # Add 1 to the stack
            in_string = True  # Start a new group
        else:
            in_string = False  # End of the previous group

        if char == ")":
            if stack:
                stack.pop()  # remove the spurious close
            result.append(stack.pop())
        maximum nesting level in the list
        return result
```
This function uses a stack to keep track of the open parentheses encountered and adds one to the stack when an open parenthesis is encountered. It also removes one from the spurious close when a closing parenthesis is encountered. The maximum nesting level is the maximum length of the stack. The function returns a list containing the maximum nesting level for each group of parentheses in the string.