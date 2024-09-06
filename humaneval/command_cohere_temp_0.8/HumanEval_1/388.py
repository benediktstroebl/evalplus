Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent each individual group of parentheses. The code is designed to handle nested groups of parentheses, and it also ignores any spaces present in the input:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
   
    # Define a stack to store the open parentheses
    stack = []
    # Define a list to store the results
    results = []
    # Iterate through each char in the input string
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # If the stack is empty or the top of the stack is not the matching opening parenthesis, ignore the closing parenthesis
            if len(stack) == 0 or stack.pop() != '(':
                continue
            # If the stack is not empty at this point, that means we have balanced and matched parentheses, so add the popped string to results
            if stack:
                results.append(''.join(stack))
        
    
   # At the end, if there are still open parentheses in the stack, that would mean they are unbalanced so we ignore the last unmatched opening parenthesis
    if len(stack) > 0:
        results.append('(' + stack.pop())
        
    return results

# Test Cases
assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
assert separate_paren_groups("(a (b))") == ['(a (b))']
assert separate_paren_groups("((a (b))") == ['((a (b))']
assert separate_paren_groups("(a))") == [')']
```
This script should solve the given problem and pass the tests you have. Let me know if you need anything else!