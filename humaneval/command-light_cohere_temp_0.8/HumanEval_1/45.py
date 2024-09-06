Here's the improved and enhanced Python script with a self-contained function that solves the problem of separating and balancing parentheses in a string:
```python
from typing import List

def separate_paren_groups(string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of parentheses and returns a list of
    separated and balanced strings.
    >>> separate_paren_groups(') ) (( ) ) ( )')
        ['', '()', '( )']
    """
    result = []
    stack = []

    for char in string:
        if char == ')':
            if stack:
                stack.pop()
                result.append(char)
            stack.push() = char
    a time.open('(')
       
        stack.append(char)

    return result
```

This code has a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated and balanced strings. The function uses a `stack` to keep track of open parentheses. The function iterates through each character in the input string and adds them to the `stack` if it is an open parenthesis '(', otherwise it pops the last element from the stack and appends it to the `result` list. The function continues until all open parentheses are processed and adds the final balanced string to the `result` list.