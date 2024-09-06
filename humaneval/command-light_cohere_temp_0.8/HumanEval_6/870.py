```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    # Split the string into a list of parentheses groups
    groups = [p for p in parentheses_string.split(' '(' )]
    
    # Initialize an empty list to store the deepest level of nesting
    nested_levels = []

    # Initialize the first level of nesting with the first group
    nested_levels.append(1)

    # Iterate through the list of groups
    for i, group in enumerate(groups):
        # Initialize the current level of nesting with an empty list
        current_level = []

        # Iterate through each element of the group
        for j, char in enumerate(group):
            if char == ')':
                # If the current element is a closing parenthesis, add the current level to the deepest level of nesting
                current_level.append(nested_levels[i])
                nested_levels.append(j + 1)
            elif char == '(':
                # If the current element is an opening parenthesis, add it to the current level of nesting
                current_level.append(j)
        nested_levels.append(1)
        return nested_levels
```
The provided Python script defines a function `parse_nested_parens` that takes a string of parentheses as input and returns a list of the deepest level of nesting for each group of parentheses. The script then uses a `split()` method to split the input string into a list of parentheses groups. It iterates through list of groups to create an empty list `nested_levels`, and appends each group to the `nested_levels` list. For each opening parenthesis, it adds it to the current level of nesting, and for each closing parenthesis, it adds the current level to the deepest level of nesting in the `nested_levels` list. The script then returns this list of nested levels.