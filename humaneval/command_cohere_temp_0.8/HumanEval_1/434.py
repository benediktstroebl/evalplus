Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent each individual group of parentheses. The script also includes a test case to demonstrate how the function works:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    if not paren_string:
        return []

    stack = []
    current_group = []
    inside_string = False
    for char in paren_string:
        if char == "'":
            inside_string = not inside_string
        elif char == "(" and not inside_string:
            stack.append(current_group)
            current_group = []
        elif char == ")" and not inside_string:
            if not stack:
                return []
            current_group = stack.pop()
        elif char == "(" and inside_string:
            current_string += char
        elif char == ")" and inside_string:
            current_string += char
        else:
            current_group.append(char)

    return stack[:-1]

# Test case
assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
```

This script features a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of substrings, each containing a single group of parentheses. The function initializes an empty list called `stack` to store the current subgroups, and another empty list called `current_group` to store the currently processed subgroups. It then iterates through the input string, checking if each opened parenthesis has a matching closed parenthesis and storing them in the correct balance. Lastly, the function returns the collected subgroups.

The included test case demonstrates the function's behavior on a sample input, asserting that the function output matches the expected result. Adjustments can be made to the test case to cover a variety of input scenarios and ensure the function's correctness under different situations.