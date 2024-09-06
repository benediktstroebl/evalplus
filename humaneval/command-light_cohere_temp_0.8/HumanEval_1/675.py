Here's the Python script with the self-contained `separate_paren_groups` function and its corresponding tests:
```python
import unittest
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Return a list of separate parenthesis groups.
    Each group should be balanced (each open brace is properly closed) and not nested within the others.
    Ignore any spaces in the string.
    """
    groups separated by unbalanced parentheses are:
    ['(',)', '())', '(()', '(',')']
    """
    # Create an empty list to store the output groups
    result = []

    # Iterate through each character in the string
    for char in paren_string:
        # If char is a closing parenthesis
        if char == ')':
            # If the group is not finished, create a new list element with the current group
            result.append(''.

        # If unbalanced group. If char is an opening parenthesis, finish the group
        elif char == '(':
            result.append(')')

    # Add the unbalanced group to result list
        else:
            result.append(char)

    # Return the list of separate parenthesis groups
    return result

class TestParentheses(unittest.TestCase.TestCase):
    """ Test cases for the
    test_groups = separate_paren_groups('( ) (( )) (( )( ))')
    assert test_groups == ['()', '(())', '(()())']
    """

To run the above code, ensure you have the `unittest` module installed. You can install it `pip install unittest` or use the `pip install` command within your terminal or command prompt. 

Please note that the code assumes that the `separate_paren_groups` function is defined and implemented as shown above.