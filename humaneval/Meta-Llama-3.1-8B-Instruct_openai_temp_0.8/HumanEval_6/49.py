```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input, 
    where each group of parentheses is separated by a space.
    It returns a list of integers, where each integer represents 
    the deepest level of nesting of parentheses in each group.

    Args:
        paren_string (str): A string of nested parentheses.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting.
    """
    
    def calculate_depth(paren_str: str) -> int:
        """ Helper function to calculate the depth of a single group of parentheses. """
        depth = 0
        max_depth = 0
        for paren in paren_str:
            if paren == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif paren == ')':
                depth -= 1
                if depth < 0:
                    raise ValueError("Invalid parentheses")
        if depth!= 0:
            raise ValueError("Invalid parentheses")
        return max_depth

    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Calculate the depth of each group and return the results
    return [calculate_depth(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a helper function `calculate_depth` to recursively calculate the depth of a single group of parentheses. It then uses a list comprehension to apply this function to each group in the input string. The result is a list of integers representing the deepest level of nesting for each group. The script also includes error checking to ensure that the parentheses are valid (i.e., that every opening parenthesis is matched with a closing parenthesis).