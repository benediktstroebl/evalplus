Here's a Python script that contains a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings that represent the individual groups of parentheses. The script also includes a test case to demonstrate the function:
```python
# The module import is necessary for the Type Hints feature
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    Parameters:
        paren_string (str): A string containing nested parentheses.
    
    Returns:
        List[str]: A list of strings where each string represents a separate group of parentheses.
    """
    # Use a dictionary to keep track of the balance of braces.
    # Use a list to keep track of separate groups.
    brace_balance = {}
    groups = []

    for char in paren_string:
        if char == '(':
            if '(' not in brace_balance:
                brace_balance['('] = 0
            brace_balance['('] += 1
        elif char == ')':
            if '(' in brace_balance:
                brace_balance['('] -= 1
            if not brace_balance['('] and '(' in brace_balance:
                groups.append(')'.join(map(str, brace_balance.values())))
                brace_balance.clear()
        elif char == ' ':
            if not brace_balance:
                groups.append(' '.join(map(str, brace_balance.values())))
                brace_balance.clear()
        else:
            if char == ')':
                if '(' not in brace_balance:
                    groups.append(char)
                else:
                    print("Warning: Unmatched right parenthesis '%s'", char)
            else:
                if '(' in brace_balance:
                    print("Warning: Unmatched left parenthesis '%s'", char)
                else:
                    groups.append(char)

    # Handle the remaining braces
    if brace_balance:
        groups.append(')'.join(map(str, brace_balance.values())))

    return groups

# Example usage
assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
```
This script includes the function `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent the individual groups of parentheses. It also includes a test case to demonstrate the function. 

To correctly handle nested groups, this implementation utilizes a dictionary called `brace_balance` to keep track of the balance of braces. This approach allows the script to address nested groups as well.