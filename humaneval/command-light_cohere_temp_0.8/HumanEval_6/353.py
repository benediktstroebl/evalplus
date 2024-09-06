```python
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    for char in parent_string:
        if char == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(0)
            else:
                result.append(parse_nested_parens(stack.pop()))
        stack.
    return result

```
This Python code defines a function called `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. 

The function uses a stack to keep track of open parentheses and maintains a list of closed parentheses, called the `result` list. The function iterates through each character in the input string, and if the character is an open parenthesis `(`), it adds one to the stack. If the character is a closed parenthesis, it checks if the stack is empty, which means that there are no more levels of nesting left in the expression, so the function appends a value of 0 to the `result` list. If the stack is not empty, the function pops the topmost element from the stack, which corresponds to the innermost most nested parentheses, and appends the result of the corresponding `parse_nested_parens` function to the `result` list. 

This is a self-contained function that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting in the parentheses.