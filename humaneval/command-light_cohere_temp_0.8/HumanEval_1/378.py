Here is a self-contained Python script that solves the problem of separating out different groups of parentheses in a given string:
```python
from typing import List

def separate_paren_groups(string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Return a list of separate strings.
    """ Remove out each group of parentheses, balancing them and without any spaces.
    """
    list of separate strings
    """
    stack = []
    result = []
    for char in string:
        if char == '(': 
            stack.append(char)
        else: 
            while stack and stack[-1] == '(': 
                result.append(stack.pop())
                pop thebr result to the stack.  to keep the adding each open parenthesis.
    return result
 list of separate strings
``` 
This function takes a string as input and returns a list of strings, each representing a separate group of parentheses in the input string. The function uses a stack data structure to keep track of open parentheses and closes them correctly.