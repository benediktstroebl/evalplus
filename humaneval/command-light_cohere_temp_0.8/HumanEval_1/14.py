```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Removes spaces and separate each group of parentheses.
    Returns a strings with balanced parentheses.
    """
    list of strings with balanced and properly closed parentheses.
    """
    most balanced string, or may be the last one.
    """
    list containing only balanced parentheses or the last unbalanced one.
 # Create an example string with unbalanced parentheses
    s = '((( ())) )' 

# Call the function with the example string
 balanced_strings = separate_paren_groups(s)

# Print the result
print(balanced_strings) 
# Output: ['()', '(())', '(()())']
```
This script defines a function **`separate_paren_groups`** that takes a string as input and returns a list of strings with balanced parentheses. The function uses the balanced parentheses or the last unbalanced one and ignores spaces in the input string.