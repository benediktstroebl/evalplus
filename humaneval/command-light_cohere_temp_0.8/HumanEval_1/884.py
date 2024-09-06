Certainly, here is the self-contained Python script that solves the problem of separating and unravelling parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    A function to separate and unravelish the given string containing parentheses.
    Args:
        string: containing multiple groups of parentheses
    Returns:
        List of unravelled strings.
    """
   
    unravelled string:
    """
    # Split the string into individual characters
    characters = s.split()
    
    # Groupify the Group is a list of characters and the corresponding opening parenthesis
    group_chars = [c for c in characters if c in '([{')]']
    
    # Initialize an empty list for the result
    result = []
    
    # Iterate through the characters and their corresponding opening parenthesis
    for c, opening in zip(group_chars, characters):
        # If the character is not a closing parenthesis, add it to the result list
        if c != ')':
            result.append(c)
    
    # Reverse the string to get the original string with proper grouping
    return result[::-1]

# Unit tests
def test_separate_paren():
    s = r"(\( )((()))"
    expected = ["()", "(())", "(()())"]
    result = separate_paren_groups(s)
    assert result == expected
```

This script defines a function `separate_paren_groups` that takes a string as input and returns a list of unravelled strings. The function uses a array of characters and their corresponding opening parenthesis to identify the groups and then appends the characters of each group to the result list. Finally, the function is reversed to get the original string with proper grouping.