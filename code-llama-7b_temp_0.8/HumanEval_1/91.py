from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # special cases
    if paren_string == '':
        return ['']

    # O(n) time, O(n) space
    def recursive_paren_groups(paren_string):
        paren_string_length = len(paren_string)

        # look for opening parenthesis
        for idx in range(paren_string_length):
            if paren_string[idx] == '(':
                # initialize new string
                current_paren_group = ''
                current_paren_group += paren_string[idx]
                # look for closing parenthesis
                for paren_idx in range(idx+1, paren_string_length):
                    if paren_string[paren_idx] == ')':
                        current_paren_group += paren_string[paren_idx]
                        # return if we are balanced
                        if len(current_paren_group) % 2 == 0:
                            return [current_paren_group] + recursive_paren_groups(paren_string[paren_idx+1:])
                        else:
                            break
        return []

    return recursive_paren_groups(paren_string)

