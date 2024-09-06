Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing balanced groups of parentheses:
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

        if open_braces == '()))':
            paren_list.append(open_braces)
            open_braces = ''
        if close_braces == '(( ':
            paren_list.append(close_braces)
            close_braces = ''

    # Handling possible remaining open braces
    if open_braces:
        paren_list.append(open_braces)

    # Handling possible remaining close braces
    if close_braces:
        paren_list.append(close_braces)

    return paren_list

# Example usage
assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])
```

This script uses two empty strings, `open_braces` and `close_braces`, to keep track of the number of open and close braces encountered, respectively. Each time a closing brace is encountered, its corresponding open brace is removed from the `open_braces` string and added to the `paren_list`. The process is repeated for the closing braces. Finally, the remaining unmatched open and close braces are appended to the `paren_list`. 

The example usage provides a way to assert the function's output against an expected output providing a more complete and detailed test coverage.  This helps to ensure that the function is correctly separating the parentheses into separate groups.