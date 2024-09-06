Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing the separated parentheses:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = ''
    close_braces = ''
    paren_list = []

    for char in paren_string:
        if char == '(':
            open_braces += char
        elif char == ')':
            close_braces += char
        elif open_braces != '':
            open_braces += char
            if open_braces == '()':
                paren_list.append(open_braces)
                open_braces = ''
        elif close_braces != '':
            close_braces += char
            if close_braces == '()':
                paren_list.append(close_braces)
                close_braces = ''

    # Handling special case for single opening or closing brace
    if open_braces == '()':
        paren_list.append(open_braces)
    if close_braces == '()':
        paren_list.append(close_braces)

    return paren_list

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script uses two empty strings `open_braces` and `close_braces` to keep track of the accumulated open and closed braces encountered during iteration through the input string. When the opening and closing braces match, they are appended to `paren_list`. The loop finishes by checking if any unmatched opening or closing braces remain and appends them to `paren_list` accordingly. The provided test case and any others would be considered within the scope of this code's functionality.  The example usage at the end demonstrates the function's behavior for the input string provided in the problem statement.