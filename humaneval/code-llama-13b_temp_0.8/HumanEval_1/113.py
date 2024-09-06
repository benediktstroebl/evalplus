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
    index = 0
    while index < len(paren_string):
        # we will be looking for open brace
        if paren_string[index] == "(":
            # if we found an open brace, lets find its pair
            next_index = find_pair(paren_string, index)
            # if we found its pair, append it to the result
            if next_index != -1:
                result.append(paren_string[index : next_index + 1])
                # move the index to next position
                index = next_index + 1
            # if we didn't find the pair, its an error, break the loop
            else:
                break
        # if its not an open brace, just move to the next position
        else:
            index += 1
    return result

