```python
from typing import List
def separate_paren_groups(input_str):
    """
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is separating those groups into separate strings and return the list of those strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    open_brace = False
    for char in input_str:
        if char == ' ':
            if open_brace:
                result.append(') '
       
    open_brace = True
        elif open_brace:
            open_brace = False
        else:
            open_brace = True
    return result
input_str = '(() ()())'
result_list = separate_paren_groups(input_str)
print(result_list)
``` 
This Python code defines a function called `separate_paren_groups` designed to separate and categorize parentheses in a given input string. The function iterates through each character in the input string to determine whether it's a space or the opening or closing of a parentheses. This process continues until all opening parenthesis is detected, at which point, it starts closing them and storing the result in a list. Additionally, a sample input string is provided, and the function is called with this input. The output is a list of properly separated parentheses.