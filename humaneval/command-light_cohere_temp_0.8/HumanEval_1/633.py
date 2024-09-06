```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns a list of parenthesis-grouped strings.

    Args:
        string s: The input string containing multiple groups of parentheses.

    Returns: list of strings:
    """
    # Define a helper function to split a string by spaces
    def split_string(string): 
        return string.split()

    # Create an empty list to store the separated strings
    result = []

    # Iterate through each group of parentheses
    for i in range(0, len(s), 2):
        # Find the close and open parentheses
        close, open = s[i:i+1], s[:i]
        # Check if the open parenthesis is balanced
        if close == '(' and open == ')':
            # If it is, append the content to the new string
            result.append(split_string(open))
        elif close != '(' and open != ')':
            # If it is not balanced, ignore it
            pass
    return result
```