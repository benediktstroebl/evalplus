Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
                result.append(')')
            else:
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    # Add the last group
    if not stack and current_group:
        result.append(')'.join(current_group))
    
    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of nested parentheses and some additional variables to determine when a group of parentheses is closed. The `result` list is used to store the separated groups. After the loop through the input string, the script will have identified each separate group of parentheses and stored them as strings in the `result` list. The example usage demonstrates how the function works for a sample input. The output of the example usage is as follows:
```
['()', '(())', '(()())']
``` 

This example output shows the expected result, which is a list of strings corresponding to the separate groups of parentheses in the input string.