Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

The function works by using the splitting and stripping approach to iterate through the string, add an opening parenthesis to a temporary string when an opening parenthesis is encountered, add a closing parenthesis to the temporary string when a closing parenthesis is encountered, and add the temporary string to the list when the balance is zero (meaning the group is fully enclosed). 

The expected behavior for the input string `'( ) (( )) (( )( ))'` is for the function to return `['()', '(())', '(()())']`. 

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

    opening_balance = 0
    temp_string = ''
    paren_list = []

    for char in paren_string:
        if char == '(':
            opening_balance += 1
            temp_string += char
        elif char == ')':
            opening_balance -= 1
            temp_string += char
        elif char == ' ':
            continue

        if opening_balance == 0:
            paren_list.append(temp_string)
            temp_string = ''
            opening_balance = 0

    if opening_balance > 0:
        paren_list.append(temp_string)

    return paren_list

# Test cases
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
assert separate_paren_groups('((a))') == ['(())']
assert separate_paren_groups('()') == ['()']
assert separate_paren_groups('(abc') == ['(abc']
```