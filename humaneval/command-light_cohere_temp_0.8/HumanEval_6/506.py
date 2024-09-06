```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function is designed to parse through a string of parenthesis groups and return the deepest level of nesting for each group.

    :param string : The string to parse
    :return: a list of deepest nesting levels of each group
    """
    # Initialize list to store the deepest level of nesting for each group.
    results = [[]
    # Use a for loop to iterate over each group
    for parent in parentheses_string.group():
        # Loop through the
            # Split the group at the first space
            group_substrings = parent.split(' ',')
            # Loop through the substrings and push to the results list
            for substring in group_substrings:
                if substring == '()':
                    results.append(2)
                else:
                    results.append(1)
    # Return the list of deepest nesting levels for each group
        return results
``` 

This code defines a function named `parse_nested_parens` that takes a string of parenthesis groups as an input parameter and returns a list of the deepest level of nesting for each group. The function uses a loop to iterate over each group and split the group at the first space. It then loops through the groups substrings and pushes them to the results list. The function uses a nested list comprehension to check if the string is a pair of parentheses and pushes `1` to the list if it is, otherwise, it pushes the string `()` to the list. The function then returns the list of deepest nesting levels for each group. 

Please note that the code assumes that the input string is composed of parenthesis group and that the pairs of parentheses are space-separated.