from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # ----------------------
    # Write your code here
    # ----------------------
    # Opening Brackets
    opening_brackets = ["(", "[", "{"].sort()
    # Closing Brackets
    closing_brackets = [")", "]", "}"].sort()
    # Stack
    stack = []
    # Balanced parentheses
    balanced_parentheses = []
    # String
    string = paren_string

    for char in string:
        # Push
        if char in opening_brackets:
            stack.append(char)

        # Pop
        elif char in closing_brackets:
            if len(stack) > 0:
                last_char = stack.pop()
                if char == closing_brackets[opening_brackets.index(last_char)]:
                    balanced_parentheses.append(f"{last_char}{char}")
                else:
                    return []
            else:
                return []

    # Empty String
    if len(stack)
