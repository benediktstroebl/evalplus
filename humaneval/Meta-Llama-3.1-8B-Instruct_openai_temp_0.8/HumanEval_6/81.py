```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of parentheses groups separated by spaces.
    It returns a list of maximum levels of nesting for each group.

    :param paren_string: A string of groups of parentheses separated by spaces.
    :return: A list of maximum levels of nesting for each group.
    """
    groups = paren_string.split()
    levels = []

    for group in groups:
        level = 0
        max_level = 0
        for char in group:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        levels.append(max_level)

    return levels


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

In this script, we first split the input string into groups using the `split` method. Then, for each group, we initialize a `level` variable to keep track of the current nesting level and a `max_level` variable to keep track of the maximum nesting level encountered so far. We iterate over the characters in the group. If we encounter an opening parenthesis, we increment the `level` and update `max_level` if necessary. If we encounter a closing parenthesis, we decrement `level`. Finally, we append the `max_level` to the `levels` list after processing each group. The function returns the `levels` list.