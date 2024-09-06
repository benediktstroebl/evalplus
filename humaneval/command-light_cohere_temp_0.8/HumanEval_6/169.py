```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string with nested parentheses as its input and returns a list of deepest nesting levels.
    Args:
        parent_string (str): The input string with nested parentheses
    Returns:
    list: A list of deepest nesting levels.
    """
    def get_parent_level(level, char):
        if char == '(':
            return level + 1
        elif char == ')':
            return level - 1
        else:
            return level

    levels = []
    for i, char in enumerate(parent_string):
        level = get_parent_level(0, char)
        levels.append(level)
    return levels[::-1]
    ```
This Python code defines a function called `parse_nested_parens` that takes a string as input and returns a list of the deepest nesting levels of parentheses in the string. The function uses a list comprehension to iterate through each character in the string. Then, it defines a helper function `get_parent_level` that returns the parent level of a given character. 

The `get_parent_level` function uses the `level` and `char` parameters to return the parent level of the character '(')' or ')' if the `char` is '(', else it returns the `level` unchanged. The `parse_nested_parens` function uses the `get_parent_level` function to find the parent level of each character in the string. 

The function then iterates through each character in the string using the `enumer` function and the `get_parent_level` helper function. It keeps track of the highest level of nesting by appending it to the `levels` list. Finally, the function returns the list of levels in reverse order using the slicing operation `levels.append(level)`.