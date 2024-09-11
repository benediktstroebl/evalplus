```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    Args:
    paren_string (str): A string of parentheses groups separated by spaces.
    
    Returns:
    List[str]: A list of strings, each representing a separate group of parentheses.
    
    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Generate all possible combinations of the input string
    for r in range(1, len(paren_string) + 1):
        for i in range(len(paren_string) - r + 1):
            groups.append(paren_string[i:i+r])
    
    # Filter out the groups that are not balanced
    balanced_groups = []
    for group in groups:
        stack = []
        for char in group:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                balanced_groups.append(group)
    
    return balanced_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a brute force approach to generate all possible combinations of the input string, and then filters out the groups that are not balanced. This approach is not very efficient for large inputs, but it should work for the provided example. If you need a more efficient solution, you could use a stack to keep track of the parentheses in each group, and a dynamic programming approach to generate the groups.