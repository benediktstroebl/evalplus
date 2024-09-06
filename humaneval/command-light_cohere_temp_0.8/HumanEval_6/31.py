```python
def parse_nested_parens(parenthes): 
    stack = []  # Stack to track nesting level
    
    for char in parenthes:
        if char == '(': 
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                raise ValueError("Unmatched closing parenthesis")
            elif len(stack) == 1:  # Match closing parenthesis with first element of stack
                stack.pop(stack[0] )
            else:  # Match closing parenthesis with a non-first element of stack
                stack.pop(stack[-1])
        else:  # Invalid character, ignore and continue parsing
            pass
    
    if len(stack) != 0:
        raise ValueError("Unexpected content after last closing parenthesis")
    
    return stack

# Example usage:
 parsed_content = parse_nested_parens('(()()) ((())) () ((())()())')')
 print(parsed_content)
```