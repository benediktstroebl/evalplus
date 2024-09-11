```markdown
### Nested Parentheses Parser

#### Problem Description

Parse a string of nested parentheses to find the deepest level of nesting in each group.

#### Code

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    :param paren_string: A string of nested parentheses groups separated by spaces.
    :return: A list of deepest nesting levels for each group.
    """
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize a list to store the deepest nesting levels
    nesting_levels = []
    
    for group in groups:
        # Initialize a counter to track the current nesting level
        nesting_level = 0
        
        # Initialize a counter to track the maximum nesting level
        max_nesting_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the nesting level
            if char == '(':
                nesting_level += 1
                # Update the maximum nesting level if necessary
                max_nesting_level = max(max_nesting_level, nesting_level)
            # If the character is a closing parenthesis, decrement the nesting level
            elif char == ')':
                nesting_level -= 1
        
        # Append the maximum nesting level to the result list
        nesting_levels.append(max_nesting_level)
    
    return nesting_levels

#### Example Usage

# Test the function with the provided example
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

#### Output

```
[2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses groups as input and returns a list of deepest nesting levels for each group. The function iterates over each group, counting the maximum nesting level by maintaining a running total of the number of opening and closing parentheses. The result is a list of maximum nesting levels for each group.