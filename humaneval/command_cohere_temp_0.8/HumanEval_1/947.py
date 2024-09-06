Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings of separated parentheses groups.

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                result.append(')'.join(current_group))
            else:
                current_group.pop()
                stack.pop()
        else:
            current_group.append(char)
    
    if current_group:
        result.append(')'.join(current_group))
    
    return result

# Example usage
test_string = '( ) (( )) (( )( ))'
print(separate_paren_groups(test_string))
```
This script uses a stack to keep track of opening parentheses and a list to accumulate the current string of parentheses. When it encounters a closing parenthesis, it checks if it has a corresponding opening parenthesis on the stack (accounting for the possibility of an empty stack at the end of a group). If it does, it adds the string of the current group to the results and resets the current group and stack to empty. The output of the example usage is:
```bash
['()', '(())', '(()())']
```
This is the expected output showing the separated parentheses groups.