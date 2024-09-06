Here is a Python script that includes a self-contained function that solves the problem:
```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    This function is designed to take a list of strings as input, where each string represents a potential parenthesis-group.
    Your goal is separate each group of parentheses into individual strings and return the list of those strings.
    Input:
    list of strings
    Output:
    list of separated strings containing only parentheses
    """
    output = []
    for item in parentheses:
        if item.count("(") > item.count(")") or full_match("("): "):
            output.append("(")
       
        else:
            output.append(")" + item)
    output.return list of a strings
```