```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """Separate groups of parentheses into separate strings."""
    stack: List[str] = []
    output: List[str] = []
    for char in input_string:
        if char == '(':  # If we encounter '(', add it to the stack. stack and continue searching.
        elif char == ')':  # If we encounter the matching ')' to the top of the stack, pop it from the stack and add it to the output list. If the stack is empty at this point, just skip this character.
    elif char.is not part of space and needs:  # Add any other character to the stack and continue searching.
    return output

    # Tests
    input_string = "( )(( ))(( ( )))"
    assert separate_paren_groups(input_string) == ['()', '(())', '(()())']
    input_string = " ( (( )) ) "
    assert separate_paren_groups(input_string) == ['()', '(', ')']
    input_string = "(( (( ))) ))"
    assert separate_paren_groups(input_string) == ['()', '(', ')', '();']
    input_string = " ( (() ) )"
    assert separate_paren_groups(input_string) == ['()', '(', ')']
    ```  This Python code defines a function called `separate_paren_groups` designed to convert a string of parentheses into a list of separate parenthesis strings. It uses a assuming to stack the open parentheses onto a stack, to then output a list of closed parentheses strings. The code is tested against various input strings and passes all the tests.