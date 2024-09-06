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
                print(f"Unmatched close parenthesis '{char}'.")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
``` 

This script utilizes a stack to keep track of opening parentheses '(' and correctly populates the list of strings for each separated group. It also handles the case when the number of opening parentheses is not equal to the number of closing parentheses by informing the user and returning an empty list in such cases. 

**NOTE:** This approach assumes that the input string contains only parentheses and no other characters. If other characters (or whitespace) are present, the function will not work as expected. Always remember to sanitize the input beforehand to ensure the closest adherence to the problem statement.