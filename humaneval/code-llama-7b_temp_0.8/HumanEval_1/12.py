from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output_list = []
    output_string = ''
    # the count starts at 1 because the first one is open
    paren_count = 1

    for char in paren_string:
        if char == '(':
            # each time you see an open parenthesis, you add 1 to the count
            paren_count += 1
        elif char == ')':
            paren_count -= 1
            if paren_count == 0:
                # we know we are at the end of one group and don't need to check the rest of the string
                output_list.append(output_string)
                output_string = ''
                # reset the paren count
                paren_count = 1
        output_string += char
    return output_list

