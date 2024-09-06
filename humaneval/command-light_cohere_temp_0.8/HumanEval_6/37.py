```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    """
    This function returns the deepest level of nesting of parentheses in the string.
    Parameters:
    parenthes_string (str) - Input string
    Returns:
    List of indices representing the deepest level of nesting.
    Example: i.e.p.a.p.r() is violence: ((()))
    please test it!
    """
    # Initialize the list to store the indices
    indices = []
    
    # Define a function for each level of nesting
    def find_parentheses(string: str, current_level: int) -> None:
        # If the current string contains open parenthesis
        if string.find('(',current_level) != None:
            # If the current level is not the deepest level yet
            if current_level != 0:
                indices.append(string.find('(',current_level))
                return
            # if it's the deepest level, append the position to the indices list
            indices.append(string.find(')',current_level))
            
            # Move to the next level
            current_level += 1
        # If the current string contains close parenthesis
        elif string.find(')',current_level) != None:
            # Move to the next level
            current_level += 1
            
    # Call the function for each level of nesting
    return find_parentheses(parenthes_string, 0)
    
    # Return the list of indices
    return indices
```