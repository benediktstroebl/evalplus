Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent the separate groups of parentheses. The code is designed to handle nested and balanced parentheses, and it ignores any spaces in the input string. 

The solution uses a stack-based approach coupled with a parenthesis checker function to correctly identify and separate the nested parenthographic groups:
```python
from typing import List

def is_parenthesis(c: str) -> bool:
    return c == '(' or c == ')'

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result: List[str] = []
    stack = []
    for char in paren_string:
        if is_parenthesis(char):
            stack.append(char)
        else:
            # If we see a closing parenthesis when there's nothing to close, return an empty list
            if not stack or stack.pop() != char:
                return []
            if not stack:
                result.append("")
                continue
            opening_char = stack.pop()
            result.append(opening_char + char)
    # Check for remaining open parentheses
    while stack:
        result.append("")
    return result
```

The script includes a standalone function `is_parenthesis` that checks whether a given character is a parenthesis, which can be used for other similar checks in other contexts. The `separate_paren_groups` function uses a list called `result` to store the final list of strings, and a stack to keep track of the currently open parentheses. It iterates through the input string and pushes each opening parenthesis onto the stack. When a closing parenthesis is encountered, the code checks if it matches the most recent opening parenthesis on the stack. If it does, both parentheses are popped from the stack, and the string between them is added to the result list. If the closing parenthesis doesn't match the expected opening parenthesis, an empty list is returned, as the groups are not properly balanced. Finally, after processing the entire string, if there are any remaining open parentheses on the stack, an empty string is added to the result list to account for the imbalance. The final result list is returned after this process.