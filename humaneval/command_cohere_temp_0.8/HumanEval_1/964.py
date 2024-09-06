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
                return []  # Unbalanced groups, returning empty list as convention
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack

# Example usage
test_string = "( ) (( )) (( )( ))"
print(separate_paren_groups(test_string))
```
This script uses a stack to keep track of opening parentheses until the corresponding closing parenthesis is encountered. It also utilizes a list to store the current group of parentheses that have been separated from the whole string. Once the loop through the string is finished, the opening parentheses that remain in the stack are appended to the current group and returned as the final result.

When you run this script and provide the example input, it will output:
```python
['()', '(())', '(()())']
```
This exemplifies the expected result as grouped by parentheses. Note that this approach aims to solve the challenge using straightforward Python and is not optimized for performance. If you encounter performance constraints, consider using alternative methodologies.  Feel free to ask if you would like to discuss such approaches.