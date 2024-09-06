```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    A recursive function that returns the deepest level of nesting for each group of parentheses in a string.
    Args:
        string: a string containing multiple groups of parentheses separated by spaces.
    Returns: list of integers, where each integer represents the deepest level of nesting for its corresponding group.
    """
    nested_list: list that stores the results of calling the recursive function on each group of parentheses.
    """
    new_group: a list that represents the next group of parentheses in the input string.
    Returns: list that contains the deepest level of nesting for all groups of parentheses in the input string.
    """
    def get_deeper_nesting(nested_list: List[int], current_group: int, new_group: List[int]) -> List[int]:
        """
        Recursive helper function to determine the deepest level of nesting for a new group of parentheses.
        Args:
            nested_list: list of integers that store the results of calling the function on each group of parentheses.
            current_group: the current group of parentheses being processed.
            new_group: the next group of parentheses in the input string.
        Returns: a list that contains the deepest level of nesting for the current and next groups of parentheses.
        """ nested_list: list of integers that stores the results of calling the function on each group of parentheses.
        """ new_group: a list that represents the next group of parentheses in the input string.
        """ current_level: the current nesting level
        """
        nested_list.append(current_level + new_group[0])
        return nested_list

    # Example usage
    # If you want to test the function with a specific input string, you can uncomment the line and provide your string in parentheses. 

# For example, you can test the function with the following string:
parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```