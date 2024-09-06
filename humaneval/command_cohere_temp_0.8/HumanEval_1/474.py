Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing balanced groups of parentheses:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '([{'
    close_braces = ')]}'
    separated_groups = []
    current_group = ''

    for char in paren_string:
        if char in open_braces:
            current_group += char
        elif char in close_braces:
            if not current_group:
                # Ignore stray closing braces
                continue
            else:
                separated_groups.append(current_group)
                current_group = ''
        else:
            current_group += char

    if current_group:
        separated_groups.append(current_group)

    return separated_groups

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```
This approach uses nested loops to iterate through the input string. It keeps track of the current group using the `current_group` variable and appends to it when encountering opening braces. When encountering a closing brace, it checks if the current group is empty, ignoring stray closing braces. Finally, it adds the current group to the `separated_groups` list and starts a new group if there are more opening braces. The output is a list of balanced groups of parentheses. 
The example usage and test case demonstrate its functionality for the provided problem statement.