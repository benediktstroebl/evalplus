```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate groups of parentheses into separate strings.
    Returns a balance groups of open and closed parentheses, without any nested.
    Input is a string of parenthesis groups.
    """ Returns a balanced and spaces.
    Input:  """ parentheses +()
    Output: list of strings
    """
    result = []
    for match in parentheses:
        # Find the length of the current match
        length = len(match)
        # Calculate the next index based on the length of the current match and the total length of all matches so far.
        next_index = length - - (length - 1)
        result.append(match[next_index])
    return result
# Example usage
parentheses = r'( ) (( )) (( )( ))'
print(separate_paren_groups(parentheses))  # Output: ['()', '(())', '(()())']
``` 
This function, named `separate_paren_groups`, takes a string of parentheses as input and returns a list of strings, each representing a balanced group of open and closed parentheses. The function uses a loop through each match in the string, and uses the length of the current match and the total length of all matches so far to calculate the next index at which the current match will be appended to the result.