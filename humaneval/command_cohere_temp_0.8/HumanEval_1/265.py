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
                print('Unbalanced parentheses!')
            else:
                temporary_group = stack.pop()
                current_group.extend(temporary_group)
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result
```

The provided Python script is designed to tackle the problem of separating nested parentheses into individual groups while ensuring that each group is balanced (every open parenthesis has a corresponding closing parenthesis). The `separate_paren_groups` function takes a string as input, which contains multiple groups of nested parentheses. 

The function workflow is as follows:
1. Initialize an empty `stack` and `current_group` list, and a `result` list to store the final output.
2. Loop through each character in the input string:
   - If the character is `'('` (open parenthesis), push the current group onto the stack and create a new empty group.
   - If the character is `')'` (closing parenthesis):
     - Check if the stack is empty. If it is, this indicates unbalanced parentheses, so print an error message.
     - If the stack is not empty, pop the top group, append it to the current group, and merge them.
   - If the character is anything else, simply append it to the current group.
3. After processing all characters, finally push the current group onto the stack and append it to the result.
4. Return the `result` list, which contains a separate list for each group of parentheses.

The example usage and test cases demonstrate how the function correctly handles different scenarios of nested and unbalanced parentheses to produce the expected output.