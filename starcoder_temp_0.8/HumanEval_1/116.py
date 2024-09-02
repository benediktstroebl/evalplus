from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # split the string into a list of individual characters
    # not a very smart method.
    char_list = [char for char in paren_string]

    # make sure there are only parentheses in the list, and not something else
    assert all(char in ["(", ")"] for char in char_list)

    # stack to hold the current group
    # group starts with an open parenthesis
    # each open paren should be matched with a close paren
    stack = [paren_string[0]]

    # output list
    output_list = []

    # loop through each character in the string
    # we'll check the last character in the stack
    for char in char_list:

        # if the last character in the stack is an open paren
        if stack[-1] == "(":

            # if the current character is a close paren
            # we've completed a group.
            if char == ")":

                # add the group to the output list
                output_list.append("".join(stack))

                # reset the stack
                stack = []

        # if the last character in the stack is a close paren
        elif stack[-1] == ")":

            # add it to the stack
            stack.append(char)

    return output_list
