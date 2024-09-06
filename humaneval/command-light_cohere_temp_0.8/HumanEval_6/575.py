```python
def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    output = []
    for char in paren_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] == 1:
                output.append(stack.pop()
           pop()
            stack.
        elif char == '(':
            stack.append(char)
        else:
            stack.append(None)
    else:
            stack.append(stack.pop())
    deeper level is the in the stack, return the highest level. 
return output
``` 

This Python function called **parse_nested_parens** takes a string of nested parentheses as input and returns a list of the deepest levels of nesting of parentheses. 

The function uses a stack to keep track of opening parentheses and closes them in the reverse order of the input string. 
The function returns the list of deepest level of nesting found in the string.