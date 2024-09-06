Here's a self-contained Python script with a function that solves the problem of separating parentheses in a multi-line string:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Function to separate groups of nested parentheses
    :param s: Input string with nested parentheses
    :return: List of separated strings
    """
    return [p.replace(make_string(' ')) for p, make_string in zip(['()', '(')', '()', ')', '(()')])
# Example usage:
input_string = '((()))()'
output_list = separate_paren_groups(input_string)
print(output_list)
```
This function takes a string `s` as input and returns a list of separated strings. The function uses a zip function to iterate over all combinations of opening and closing parentheses in the input string, and the `replace` method to replace each opening parenthesis with a single space. 
The output will be a list of strings where each one is a balanced and properly-formed parentheses.