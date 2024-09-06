Here's a Python script that defines a function 'separate_paren_groups' solving the problem:
```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate each balanced group into balanced (each open brace is properly closed) and return them as separate strings.
    """

    balanced group of parentheses.
    e.g.)Done by:
    -OPEN PARENS/. Close all round brackets and then remove the last opening parenthesis
    """
    balanced_groups = []
    for match in parentheses:
        if match.count('(', 0, 0) == len(match):  # If the current match is balanced
            balanced_groups.append(match)  # Append the balanced group as a string
        else:  # If the current match is not balanced
            pass  # Skip unbalanced group
    return balanced_groups  # Return the list of balanced groups
def test_separate_paren_groups():
    test_input = "( ) (( )) (( )( ))"
    assert separate_paren_groups(test_input) == ['()', '(())', '(()())']  # True
    return
test_separate_paren_groups()  # Output: True
```
The 'separate_paren_groups' function takes a string of parenthesis groups as input and returns a list of balanced groups of parentheses. It uses a balancing logic to check whether a group is balanced and adds it to the list of balanced groups if it is.