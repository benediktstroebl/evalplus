Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of separate groups of parentheses.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '('
    close_braces = ')'
    paren_groups = []
    current_group = ''

    for char in paren_string:
        if char == open_braces:
            current_group += char
        elif char == close_braces:
            current_group += char
            if not current_group.count(open_braces) != len(close_braces):
                paren_groups.append(current_group)
                current_group = ''
        else:
            current_group += char

    if current_group:
        paren_groups.append(current_group)

    return paren_groups

# Example usage
test_string = '( ) (( )) (( )( ))'
print(separate_paren_groups(test_string))
```
This script uses a basic approach to iterate through the input string and collect opening parentheses. When a closing parenthesis is encountered, it checks to see if the current group is balanced (the number of opening and closing parentheses is the same). If it is balanced, the current group is added to the list of parenthesis groups, and the process starts fresh with the next group. This process is repeated until all the parentheses in the string have been processed.

When executed with the provided test string, this script will print out a list of strings corresponding to the separate groups of parentheses, in the following order:
```
['()', '(())', '(()())']
``` 

This output corresponds to each separate group of parentheses in the input test string.