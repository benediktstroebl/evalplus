```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate parentheses groups into separate strings.
    Returns list of list of strings.
    """
    require balanced and balanced open and closed parentheses.
    """
    delimiter: whitespace is automatically assumed
    """
    # Create an empty list to store the separated strings
    result = []

    # Loop through each character in the string
    for char in parentheses:
        if char == ')':
            # If we encounter the first '', add the current group to the result list
            result.append('(' + '))  # String version of the group with an opening parenthesis
            # Skip the next character
            continue
        elif char == '(':
            # If we encounter an ')', add a closing parenthesis to the previous group
            result.append(')')  # String version of the group with an opening parenthesis and a closing parenthesis
            # Skip the next character
            continue
        else:
            # Add the character to the previous group
            result.append(char)

    # Return the list of separated strings
    return result
``` 

This Python function named `separate_paren_groups` takes a single argument: `parentheses`, which is a string containing multiple groups of parentheses. 

It then uses a loop to iterate through each character in the string. After each opening parenthesis is added to the result list, the closing parenthesis is added to the previous group.  This finally, the function returns a list of separated strings.