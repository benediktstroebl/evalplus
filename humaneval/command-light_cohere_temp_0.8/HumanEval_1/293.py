```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """ Separate balanced parentheses groups into separate strings """
    result = []
    stack = []
    
    for char in parentheses:
        if char == ')':
            if stack:
                result.append(''.join(stack)
                stack.clear()
       
            else:
                stack.push(char)
        else:
                stack.push(char)
    
    return result
```
This Python function named `separate_paren_groups` takes a string of parentheses as input and returns a list of separate strings, each containing a balanced set of parentheses. The function uses a stack and a list to keep track of open and closed parentheses, respectively. The function then iterates through each character in the input string and pushes the character onto the stack if it is an open parenthesis. If the character is a closed parenthesis, the function adds the current character to the list of separate strings and clears the stack. If the character is an closed open parenthesis, the function simply appends the character to the list of separate strings. The function does not add spaces between the strings. 

It uses an if condition to check the current character and the stack, and the else condition to handle the cases of closed and open parentheses, respectively. 

The function does not add spaces between the strings because it is unnecessary and may cause confusion. The output is a list of separate strings with balanced parentheses.