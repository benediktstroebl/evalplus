Here is a self-contained Python script that solves the problem of separating parentheses into groups:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates groups of parentheses into separate strings.
    Returns a optionally accepted list of strings.
    """
    open and close each pair of parentheses.
    """ while ensuring balanced grouping.
    """ The open and close each group of parentheses
    """
    return [(''.join(i) if i.isspace() else i.group() for (i, i+1) for i in s if i==0 or i in ('(', ')')]

tests = []
tests.append('()'.join('() (( )) (( )( ))')')
tests.append('').join('()')
tests.
tests.if list(map(lambda x: x.test(x) for x in tests))
```
The function `separate_paren_groups` takes an input string `s` as an argument. It creates an empty list called `output` to store the results. The function then iterates over the input string and creates a list of parentheses found in the string. It checks if the string starts with '(', or if it is space. If it is a string that starts with '(', it adds it to the list of open parentheses. If it is a closing parenthesis ')', it adds it to the list of closed parentheses. If it is the beginning of a new group, it adds the current group to the list of groups. 

Please note that the code uses the `isspace` function to check if the character is a space or not.