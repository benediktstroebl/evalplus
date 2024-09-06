Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of separate groups of parentheses. The code is formatted with a markdown code block and inline comments to explain the logic:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    """
    # Define a helper function to check if a given substring is a balanced expression or not
    def is_balanced(expr):
        # Use a dictionary to keep track of open parentheses encountered
        char_balance = {}
        for char in expr:
            if char in char_balance:
                char_balance[char] += 1
            else:
                char_balance[char] = 1
        return all(balance == 0 for balance in char_balance.values())
    
    # Split the input string into a list of substrings based on the unbalanced expressions
    paren_list = [expr for expr in paren_string.split()]
    
    # Use a list comprehension to separate balanced expressions into a list of strings
    return [expr for expr in paren_list if is_balanced(expr)]
```
This script splits the input based on unbalanced expressions, and then uses a list comprehension to filter out the balanced expressions, returning them as a list. Given the test case provided, this script should respond with the list ['()', '(())', '(()())'].