```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups of balanced parentheses into separate strings and return the list.
    Requires: Python str.split() method.
    Returns the recipe: input string must follow the following format:
        <start>*args...>*<end>
    """
    # Split the string into individual lines
    args_lines = paren_string.split('\nl')

    # Loop through each line in the string
    for line in args_lines:
        # If the line is empty, skip it (even if it has a '\n')
        if not line.strip():
            continue
        # If the line is not empty, split it into a list of spaces and parentheses
        line_parts = line.split(' ')

        # Remove any leading or trailing spaces from each part
        spaces = [part.strip() for part in line_parts]

        # If there are no parts (this should not happen in a valid string), skip this line
        if len(spaces) == 0:
            continue

        # Create the output string by joining the parts in the order they were found
        output_part = ''.join(''.join(spaces, sep=''))

        # If the current part is not the last one, add a trailing newline to the output
        if not line.islast():
            output_part += '\n'

    # Return the list of separated strings
    return [output_part]
``` 
This function takes a string of parentheses as input and returns a list of separated strings. The script is self-contained and follows the problem statement.