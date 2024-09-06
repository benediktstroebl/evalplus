```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate and return list of non-empty groups of parentheses from input string"""
    return [w for w in s.findall('([ ]*)', s) if w.count('()') > 1]
``` 
This function uses the findall() function with a regular expression to find all non-empty parenthesis groups in the string. The regular expression ([ ]*) matches any group of one or more opening parentheses, followed by zero or more closing parentheses. The count() function is used to check if the length of the matched group is greater than one, ensuring that the group is not empty. The function then returns a list of all non-empty parenthesis groups from the input string.