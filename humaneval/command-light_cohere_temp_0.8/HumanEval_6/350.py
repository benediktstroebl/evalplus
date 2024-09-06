```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function takes in a string of parenthesis groups and returns a list of the deepest level of nesting.
    Test if each input string is empty or not, throw an exception.
    Parse the string and break it into a list of groups
    For each group, we find the deepest level of nesting by iterating over each closing parenthesis and counting the number of open parentheses
    when we find a closing parenthesis, we return the deepest level of nesting as our output.
    Test the if any list of open parentheses is less than the depth of the deepest level of nesting, throw an exception
    Test if the function's output is a list of integers and returns True, otherwise False.
```