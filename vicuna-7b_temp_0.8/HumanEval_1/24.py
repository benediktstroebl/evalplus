from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # initialize an empty list to store the separated groups
    separated_groups = []

    # iterate over the string using a for loop
    for char in paren_string:
        # if the char is an open brace, we have found a group, so add it to the list and start a new group
        if char == '(':
            # if the previous character is not a close brace, add a space to the list
            if not re.search(r'(?<!))', paren_string[paren_string.index(char) - 1]):
                separated_groups.append(' ')
            # add the group to the list
            separated_groups.append(paren_string[paren_string.index(char) - 1:])

            # reset the group
            separated_groups = [']']

        # if the char is a close brace, we have reached the end of a group, so add it to the list
        # and move on to the next group
        elif char == ')':
            separated_groups.append(paren_string[paren_string.index(char) - 1:])

            # remove the closing brace from the list
            separated_groups.pop()

    # if there is only one group, it has not been separated
    if len(separated_groups) == 1:
        separated_groups.append('')

    return separated_groups