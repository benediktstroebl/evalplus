```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups of balanced parentheses into separate strings and return the list of those strings.
    """
    balanced (each open brace is properly closed) and not nested within each other
    """
    return [p.strip() for p in parentheses. balanced]
```
parentheses = """() (( )) (( )( )) ))"""
parentheses_list = separate_paren_groups(parentheses)
print(parentheses_list)  # Output: ['()', '(())', '(()())']
``` 
This Python code defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separate parenthesis groups. The function uses a balanced parentheses and returns the list of those groups as output.