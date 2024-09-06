from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    start = 0
    while start < len(paren_string):
        # Check to see if the character at the start is a valid start
        if paren_string[start] not in "()":
            # If it is not a valid start, move on
            start += 1
        else:
            # If it is a valid start, then we will continue until we find a close
            end = start + 1
            while end < len(paren_string) and paren_string[end] in "()":
                # If we find a close, then add the group to the list
                if paren_string[end] == ")" and paren_string[start] == "(":
                    result.append(paren_string[start:end + 1])
                # Otherwise, continue searching for the close
                end += 1
            # Move on to the next start
            start = end
    return result

