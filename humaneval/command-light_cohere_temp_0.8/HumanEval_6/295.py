```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting for parentheses in a given string.

    Parameters: 
    parent_string (str): The string to parse, represented multiple groups for nested parentheses separated by spaces.

    Returns: 
    list[int]: A list of the deepest level of nesting of parentheses, starting from the leftmost.
    """
    Note that the expected format is a string of nested parentheses separated by spaces.
    """
    Following are the expected format for the input: 
    '(()()) ((())) () ((()))' 
    Return value: 
    [2, 3, 1, 3]
    """

    nested_parens = []  # Initialize an empty list to store the results

    for group in parent_string.split(' ' ' ):
        if group == '(':
            nested_parens.append(1)  # Add 1 to the list to start
        while group:
            if group[0] == ')':
                nested_parens.append(len[-1])  # Append the last element of the list
                break
            else:
                nested_parens.append(2)  # Append the first element of the list
                break
        return nested_parens

    # Example usage:
    # Test string
    test_str = '(()()) ((())) () ((()))'

    # Call the parse_nested_parens function with the test string
    result = parse_nested_parens(test_str)

    # Print the result
    print(result)
```
This script defines a function called `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group. The function uses a `split` to split the string into groups of parentheses, and then uses a nested loop to iterate through each group and count the number of open parentheses. The result is then the list of closed parentheses.