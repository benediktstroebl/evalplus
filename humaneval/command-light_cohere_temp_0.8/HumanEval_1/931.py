Here is a Python script that contains a self-contained function that solves the problem of separating nested parentheses:
```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    This function takes a list of strings as input, representing a list of parenthesis groups.
    It returns a balance the multiple unbalanced parenthesis groups into separate strings,
    and the list of those strings.
    >>>
    list of strings: ['()', '((()))', '(()())']
    """
    return [p for p in parenthesis if p != '(']
``` 
This function uses a list comprehension to iterate through each string in the input list and checks if the string is not '('. If it's not, it is added to the list of separate strings. 

This function can easily be used to solve problems with separating nested parentheses in markdown code blocks, or any other text that contains parentheses.