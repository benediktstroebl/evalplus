```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns lists of parenthesis groups.

    Input to this function is a string containing multiple groups of nested parentheses.
    Return a list of strings, each representing a group of parentheses.

    Syntax:
    Input: string containing multiple groups of parentheses
    Return: list of strings, each representing a group of parentheses
    """
    return [w for w in s.groups(). all(w.isspace('(')'), w.isspace(')'))]
```

This function utilizes list comprehension to iterate over each group of parentheses in the input string. The function checks whether character '(' or ')' is part of the string using the `isspace()` method. If it is a space, it adds the character to the output list. 

Please note, this solution assumes that the input string contains only the groups of parentheses and no other characters.