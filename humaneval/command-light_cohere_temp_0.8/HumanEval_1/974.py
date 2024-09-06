Here is a Python script that contains a self-contained function that solves the problem of separating nested parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate and return groups of parentheses.
    """
    string s: str
        >>> separate_paren_groups(') ( ) (( )) (( )( ))')
        ['', '(')', '(())'']
    """
    return [part.split('()') for part in s.un if part.count('()') > 1 else]
```
This function uses the List function to split the string by spaces into a list of strings. The count of open parentheses in each string is checked to return only the group of parentheses and exclude any other string.