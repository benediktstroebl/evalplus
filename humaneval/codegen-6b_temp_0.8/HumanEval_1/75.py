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
    ind = 0
    while ind < len(paren_string):
        # find the next (, or )
        next_paren = paren_string[ind]
        if next_paren == '(':
            quote_mark = ')'
        elif next_paren == ')':
            quote_mark = '('
        else:
            raise ValueError('Non open parenthesis found')
        paren_stack = [next_paren]
        ind += 1
        while ind < len(paren_string):
            if paren_stack:
                curr_char = paren_string[ind]
                # if this is the end of a group
                if curr_char == quote_mark:
                    paren_stack.pop()
                    break

                # if this is a parenthesis, we can only append if we have seen the matching
                # paren to the top of the stack
                if curr_char == next_paren:
                    paren_stack.append(next_paren)
                else:
                    break
            ind += 1
        else:
            raise ValueError("Non matching parenthesis found")

        # this is the ending part of the string to be split
        part = paren_string[ind:ind + len(paren_stack)].strip()
        result.append(part)
        ind += len(paren_stack)
    return result

