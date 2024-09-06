from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Start with a list of empty strings
    result = ['' for _ in range(len(paren_string))]

    # Create a 2D list to keep track of the current nesting level
    nesting_level = [[0] * len(paren_string) for _ in range(len(paren_string))]

    # Loop over each character in the input string
    for i, c in enumerate(paren_string):
        # If the current character is a left parenthesis, increment the nesting level for the opening brace
        if c == '(':
            nesting_level[i//2][i%2] += 1

        # If the current character is a right parenthesis, decrement the nesting level for the closing brace
        elif c == ')':
            nesting_level[i//2][i%2] -= 1

        # If the current character is a matching closing brace, we've reached the end of a group
        if c == '(' and nesting_level[i//2][i%2] == 0:
            nesting_level[i//2][i%2] = 1
            result[i//2] = ')'

            # Update the nesting level for the next group
            for j in range(i//2, len(paren_string)):
                nesting_level[j][0] += 1

    # Return the list of separate groups
    return result