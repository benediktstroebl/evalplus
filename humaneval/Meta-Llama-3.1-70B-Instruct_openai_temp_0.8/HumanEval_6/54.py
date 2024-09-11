```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[List[int]]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[List[int]]: A list of lists where each sublist contains the deepest level of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def calculate_depth(paren_group: str) -> List[int]:
        """
        Calculate the maximum depth of a single group of parentheses.

        Args:
            paren_group (str): A string of a single group of nested parentheses.

        Returns:
            List[int]: A list containing the maximum depth of the group.
        """
        max_depth = 0
        current_depth = 0
        for paren in paren_group:
            if paren == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif paren == ')':
                current_depth -= 1
        return [max_depth]

    # Split the input string into groups of parentheses
    paren_groups = paren_string.split()

    # Calculate the maximum depth of each group
    results = [calculate_depth(group) for group in paren_groups]

    # Flatten the list of lists into a single list
    flattened_results = [item for sublist in results for item in sublist]

    return flattened_results


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```