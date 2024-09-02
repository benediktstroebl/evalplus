from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    assert isinstance(paren_string, str), "Input must be a string"
    assert paren_string.isalpha() is False, "No letters are allowed in the input string"

    # creat a list to store all the groups
    groups = []

    # create a new group to keep track of our nested group
    group = ""

    # go through the string character by character
    for char in paren_string:
        # if the character is a space, ignore it
        if char == " ":
            continue
        # if the character is an opening brace, we need to add the new group to the list and create a new group
        elif char == "(":
            groups.append(group)
            group = "("
        # if the character is a closing brace, add the character to the group and check if it is a closing brace for the
        # outermost group. if so, add the group to the list
        elif char == ")":
            group += ")"
            # check if the current group is the outermost group
            if group == "()":
                groups.append(group)
                group = ""
        # otherwise, just add the character to the group
        else:
            group += char
    # add the last group to the list
    groups.append(group)
    return groups

