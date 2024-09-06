Here is a self-contained Python script that includes the function `separate_paren_groups` that solves the problem:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string s containing multiple groups of parentheses as input.
    The goal is to separate those groups into separate strings and return the list of those strings.
    A group is open parenthesis and the closing parenthesis must be the same
    The rest of the string will be split into separate strings.
    """
    list comprehension with string matching the groups of parentheses in s
    """
    return [s[i:i+2] for i in (list([('(', ')', ''), ('(', ')', ''), ('(', ')', ''),
                                     (')', ')', '))])
    if __name__ == "__main__":
        s = "( ) (( )) (( )( ))"
        results = separate_paren_groups(s)
        print(results)
```
This script defines a function `separate_paren_groups` that takes a string as input and returns a list of strings that have been split from the given input string.