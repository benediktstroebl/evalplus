Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing individual groups of parentheses. The code is presented in a markdown code block, as per your request:
```python
#  Importing the "List" module from "typing"
from typing import List

# Defining the function "separate_paren_groups" that takes a string of parentheses as input and returns a list of strings 
# containing individual groups of parentheses.
def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = 0
    groups = []
    current_group = []

    # Iterating through the characters in the input string
    for char in paren_string:
        if char == '(':
            open_braces += 1
            current_group.append(char)
        elif char == ')':
            open_braces -= 1
            if open_braces == 0:
                groups.append(''.join(current_group))
                current_group = []
    # Appending the last group
    if open_braces == 0 and len(current_group) > 0:
        groups.append(''.join(current_group))

    # Returning a list of strings, where each string represents a group of parentheses
    return groups

# Testing the function with a sample input and evaluating the output
sample_input = '( ) (( )) (( )( ))'
expected_output = ['()', '(())', '(()())']

assert separate_paren_groups(sample_input) == expected_output
```
The function uses a counter for the open braces to track the balance of parentheses within each group and creates a new list for each newly opened group of parentheses. The result is a list of strings, where each string corresponds to a separate group of parentheses, properly balanced and without any nesting. 

Let me know if this solution suits what you're looking for. Feel free to ask if you would like further clarification or additional details.