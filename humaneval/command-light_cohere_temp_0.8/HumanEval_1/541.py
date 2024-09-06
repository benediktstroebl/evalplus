Here is a self-contained Python script that solves the problem of separating out and balancing parentheses in a given string:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups while balancing the fact balanced (each open brace is properly closed) and not nested within each other
    """
    return [ele.replace() for ele in s.group for sub in ele.group if sub!aren't '('{}' and ')'
    # Remove any spaces
    return [ele.replace(" ") for ele in s.group if sub.replace(" ", "")]
balance_group
```
This function takes a string s as input and returns a list of strings, each representing a balanced group of parentheses in s. This is done by iterating over each group of nested parentheses and creating a new string for each group, without any nested parentheses or spaces. 

The function then returns a list of these strings. This code is designed to be self-contained and does not require any external functions or variables.