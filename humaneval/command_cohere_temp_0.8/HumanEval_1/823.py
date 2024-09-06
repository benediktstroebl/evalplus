Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing the separate groups of parentheses. The code is formatted with a markdown code block, as requested:
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
            if open_braces == '))':
                paren_list.append(close_braces)
                open_braces = ''
                close_braces = ''
        elif close_braces != '':
            close_braces += char
            if close_braces == '(()':
                paren_list.append(open_braces)
                open_braces = ''
                close_braces = ''
        elif char != ' ':
            paren_list.append(open_braces + char + close_braces)
            open_braces = ''
            close_braces = ''

    # Handling edge case with trailing open braces
    if open_braces:
        paren_list.append(open_braces)

    return paren_list

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This code defines the `separate_paren_groups` function and uses a loop to iterate through the input string, keeping track of open and close braces in separate strings. When an unbalanced situation is encountered, it adds the appropriate braces to the corresponding list.  The final list also eliminates any spacing, and the function's behavior is demonstrated through an example usage. 

Note that this script assumes you have Python 3.8 or a later version, as it incorporates type hints and uses the `List` subtype. Also, keep in mind that the solution is designed to work with balanced parentheses only and doesn't handle nested or unbalanced scenarios correctly. You can adjust the code to handle such cases if needed.  If you have specific requirements or additional constraints you'd like the code to address, feel free to provide more details so that I can further refine the solution.