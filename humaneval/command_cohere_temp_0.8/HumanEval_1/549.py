Here's a Python script that contains a function called `separate_paren_groups` that takes in a string of parentheses and returns a list of strings of separate groups of parentheses. 

The function works by using a stack to keep track of opened parentheses, and whenever an opening parentheses is encountered, it pushes onto the stack. When a closing parenthesis is encountered, the function checks if the last item of the stack is the opening parenthesis which it corresponds to, and if so, it pops the stack until it finds the corresponding opening parenthesis. The function returns a list of strings that occur between each pair of corresponding opening and closing parentheses. 

The script also includes a markdown block that provides an example of input and output for the function:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack: List[str] = []
    current_string: str = ""

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                current_string += char
        else: 
            current_string += char
    
    return [current_string for _ in range(len(stack))] if stack else [current_string]

# Test cases
assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
assert separate_paren_groups("(a (b c))") == ['(a ', '(', 'b c')]
assert separate_paren_groups("(())") == ['()', '()']
assert separate_paren_groups("()") == ['()']
```