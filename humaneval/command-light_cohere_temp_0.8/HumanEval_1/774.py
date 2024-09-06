```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of opening parentheses from their corresponding groups of closing parentheses into separate strings, without nested groups.
    Input: s -- string with opening and closing parentheses.
    Output: List of strings with opening parentheses separated from their corresponding closing parentheses
    """
    return [p for p in s if p in '()()]  # return list of all opening parentheses in string s
```
This function uses a list comprehension to iterate through each character in the input string `s`. It checks if the character is a '(', returns the character as a string, and if it is not, it does nothing and returns ' ''.