```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    pattern = r"\(\)([^()]\)"
    return [match. groupings for match in pattern.match. None] if the of parentheses.
    ``` separate_string(match)
```
The function `separate_paren_groups` takes a string of parentheses (`parentheses`) as input and returns a list of separated strings. The function uses a regular expression pattern to match and separate each group of parentheses. 

The function also handles the case where there are no parentheses in the string by returning an empty list. 
Note that the pattern `r"\(\)([^()]\)"` matches any whitespace-separated string of one or more opening parentheses followed by zero or more closing parentheses or any character not in parentheses.