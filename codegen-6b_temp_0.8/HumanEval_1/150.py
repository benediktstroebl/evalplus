from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []

    for i, char in enumerate(paren_string):
        if char == '(':
            paren_stack.append(i)
        elif char == ')':
            last_open_paren = paren_stack.pop()
            # literal = paren_string[last_open_paren:i]
            string_to_separate = paren_string[last_open_paren + 1:i]
            if string_to_separate:
                separated_strings = separate_paren_groups(string_to_separate)

                if len(separated_strings) == 1:
                    return_list = []
                    return_list.append(''.join([paren_string[:last_open_paren],
                                                separated_strings[0]]))

                    if len(separated_strings) > 1:
                        return_list.append(''.join([separated_strings[0],
                                                    paren_string[i + 1:]]))

                    return return_list

    return [paren_string]

