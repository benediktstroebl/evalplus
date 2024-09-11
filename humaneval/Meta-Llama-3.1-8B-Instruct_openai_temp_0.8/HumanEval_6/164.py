```python
from typing import List
import re


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    :param paren_string: A string containing multiple groups of parentheses separated by spaces
    :return: A list of integers representing the deepest level of nesting for each group
    """
    # Split the input string into individual groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Loop over each group
    for group in groups:
        # Initialize a counter to track the nesting level
        nesting_level = 0
        max_level = 0

        # Loop over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the nesting level
            if char == '(':
                nesting_level += 1
                max_level = max(max_level, nesting_level)
            # If the character is a closing parenthesis, decrease the nesting level
            elif char == ')':
                nesting_level -= 1

        # Append the maximum nesting level for the group to the results list
        results.append(max_level)

    return results


# Test the function with the example input
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

However, there is a more concise way to solve this problem using regular expressions:

```python
from typing import List
import re


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    :param paren_string: A string containing multiple groups of parentheses separated by spaces
    :return: A list of integers representing the deepest level of nesting for each group
    """
    # Split the input string into individual groups
    groups = paren_string.split()

    # Initialize a list to store the results
    results = []

    # Loop over each group
    for group in groups:
        # Use a regular expression to find the maximum nesting level
        max_level = max(re.findall(r'\((?:[^()]|(?R))*\)', group)) - 2

        # Append the maximum nesting level for the group to the results list
        results.append(max_level)

    return results


# Test the function with the example input
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This version of the function uses a regular expression to find all occurrences of balanced parentheses in each group, and then finds the maximum nesting level by counting the number of opening parentheses. The `- 2` is used to subtract the two outermost parentheses.