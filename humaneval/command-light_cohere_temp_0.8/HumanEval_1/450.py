```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    pattern = r"\([^\)]+\)"
    return [match.group() for match in re.finditer(pattern, input_string)]
```
This function splits a string into a list of matched groups of parentheses, which are the output of the function. 

This function is well-contained, and it only uses the built-in module 're' for regular expressions and 'str' for string manipulation. 
This function can be easily adapted to other similar problems that require pattern matching.