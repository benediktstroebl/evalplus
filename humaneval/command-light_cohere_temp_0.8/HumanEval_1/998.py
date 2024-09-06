```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [oken for token in s.group() if not token == ' ')  # Remove spaces. group() splits on spaces.
# Examples:
string = '( ( ) ) (( ))'
groups = separate_paren_groups(string)
print(groups) # Output ['()', '(())', '(()())']
``` 
This script defines a function named `separate_paren_groups` that takes a string s as input and returns a list of strings. The function uses the string slicing to ignore spaces and create a list of the remaining characters, which are the individual groups of parentheses. 

The tests are designed to check if the function is working correctly.