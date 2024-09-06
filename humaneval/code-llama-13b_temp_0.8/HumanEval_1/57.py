from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Hint 1:
    # There is a stack data structure in Python that is perfect for this problem.
    # Google it and learn about it.
    # Then use it.
    # Hint 2:
    # If you don't know what a stack data structure is, here is a hint.
    # The stack data structure is just like a stack of plates.
    # Imagine you have a stack of empty plates.
    # As you encounter opening parentheses, you put a plate on the stack.
    # As you encounter closing parentheses, you remove a plate from the stack.
    # The top plate on the stack is the current group.
    # If the stack is empty when you encounter a closing parenthesis,
    # that means the parentheses are not balanced and the string is invalid.

    groups: List[str] = []
    cur_group: str = ""
    stack: List[str] = []

    # This loop goes through each character in the string
    for char in paren_string:

        # If the character is an opening brace,
        # push it onto the stack.
        if char == "(":
            stack.append(char)
        # If the character is a closing brace,
        # pop it off the stack.
        # Then append it to the current group
        elif char == ")":
            stack.pop()
            cur_group += char
        # If the character is a space,
        # ignore it
        elif char == " ":
            continue
        # If the character is a newline,
        # start a new group
        elif char == "\n":
            groups.append(cur_group)
            cur_group = ""

        # If the stack is empty,
        # start a new group
        if not stack:
            groups.append(cur_group)
            cur_group = ""

    # Add the last group to the list of groups
    groups.append(cur_group)

    return groups
