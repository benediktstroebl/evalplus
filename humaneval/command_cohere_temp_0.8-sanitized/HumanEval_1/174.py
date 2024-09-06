from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of parentheses into individual strings.

    Args:
        paren_string (str): Input string containing multiple groups of parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( ()( ))')
        ['()', '(())', '(()())']
    """

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Stack to keep track of nested parentheses
    stack = []

    # Iterate through each character in the input string
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # If stack is empty, this closing parenthesis doesn't belong to any group
            if not stack:
                separated_groups.append(char)
            else:
                # Pop all characters from the stack until the matching opening parenthesis is found
                while stack and stack.pop() != '(':
                    separated_groups.append('')
                if not stack:
                    separated_groups.append(char)
                else:
                    separated_groups.append('')

    # If there are still characters left in the stack, add them as a group
    while stack:
        separated_groups.append('')
        stack.pop()

    return separated_groups