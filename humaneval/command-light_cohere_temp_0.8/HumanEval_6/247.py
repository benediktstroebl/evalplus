```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    # Remove spaces and split by parentheses to get nested parentheses
    inps = s.replace(" ")[1:-1]
    # Initialize an empty list to store the levels of nesting
    result = []
    # Loop through the list of parentheses and create the deepest level of nesting
    for par in inps:
        if par == ")":
            result.append(3)
        elif par == "()":
            result.append(2)
        else:
            result.append(1)
    return result
```
This function, `parse_nested_parens`, takes a string of nested parentheses as input and returns a list of their depths. It uses whitespace to separate the groups of parentheses, and counts the number of parenthesis to get the depth of the nesting.

It loops through each group of parentheses and adds an entry to the `result` list if it's a ")" or a "()" to represent the deepest level of nesting.