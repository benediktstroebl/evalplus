```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    result = []
    nesting_level = 0
    for char in s:
        if char == '(': nesting_level += 1
        if char == ')': nesting_level -= 1
        if nesting_level > 0: result.add(char)
    result.append('')  # char != ' ')
    return result
``` 
This Python function, `separate_paren_groups`, takes a string `s` as input and aims to split it into a list of strings based on parentheses. 

It iterates through the input string, keeping track of the nesting level of parentheses. Once a opening parenthesis is found, it subtracts the current level from the nesting level to determine if it's the closing parenthesis. 

It then adds the current character to the list of results. 

Finally, the function returns the list of strings.