from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # 1. parse the input
    paren_string = paren_string.replace(" ", "")
    # 2. iterate through the paren_string
    current_word = []
    paren_groups = []
    for i in range(0, len(paren_string)):
        char = paren_string[i]
        # 3. append the char to the current word
        current_word.append(char)
        # 4. if the char is a closing paren, append the current word to the paren groups
        if char == ")":
            paren_groups.append("".join(current_word))
            current_word = []
    return paren_groups

