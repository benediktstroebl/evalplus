```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Function to separate and rearrange the parenthesis groups.
    The Function accepts a input string containing multiple groups of parentheses.
    Each group of parentheses are separated and rearranged into a separate string.
    Test if the string can be split into non-parentheses groups.
    """
    string splitting rules for parentheses
    """
    # Define a list to store separated groups of parentheses
    res = []

    # Iterate through each character in the string
    for char in s:
        # If the character is a '(' or ')', add it to the result list
        if char == '(':
            res.append(')')
        else:
            res.append(char)

    # Return the list of separated parentheses
    return res
# Example test cases for function's expected behavior
assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
assert separate_paren_groups('()') == ['()']
assert separate_paren_groups('()(( ))') == ['()()']
assert separate_paren_groups('(()))') == ['(())']
```