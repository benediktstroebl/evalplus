Here's a Python script that contains a function called `separate_paren_groups` which accepts a string consisting of multiple groups of nested parentheses and returns a list of these separate groups. The function works by using the `reversed` function in combination with a stack to keep track of open parentheses, while also using a queue to store the resulting separated groups:
```python
from typing import List, Iterator

import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove all spacing from the string
    paren_string = re.sub(r'\s', '', paren_string)
    
    # Separate by nested parentheses
    opener = re.compile(r'(\(|\))')
    separators = opener.findall(paren_string)
    
    # Create a reversible iterator
    iterators = [iter( separators ) for _ in range(len(separators))]
    reversible_iterators = (iter(item) for item in zip_longest(*iterators, fillvalue=None))
    
    # Initialize both a stack (to keep track of currently open parentheses) and a list to store the resulting separated groups
    stack = []
    result = []
    
    # Iterate through the reversible iterator in reverse to correctly split on parentheses
    for opener, closer in reversible_iterators:
        if opener == '(':
            stack.append(closer)  # Keep track of currently open parentheses
        elif closer in stack:
            stack.pop()  # Pop parentheses that are now closed
        else:
            current = ''.join(closer for closer in stack if closer)  # Create a string of currently opened parentheses
            result.append(current)
            stack = []  # Clear the stack for the next group
    
    # Append the last group (if there are still open parentheses)
    if stack:
        result.append(''.join(closer for closer in stack))
    
    return result
```

The provided code uses the `re` module to remove any spaces from the input string and create a reversible iterator to correctly separate the groups of parentheses. The use of a stack and a list allows the function to keep track of open parentheses and store the resulting separated groups, respectively.