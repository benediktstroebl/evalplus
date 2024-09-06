from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Find the positions where an open parenthesis is followed by a close parenthesis.
    # Ex. "(())" has 2 such positions.
    pos = [i for i, char in enumerate(paren_string) if char == ')' and paren_string[i - 1] == '(']
    # If there are no such positions, then there are no parenthesis to separate.
    if len(pos) == 0:
        return [paren_string]

    # Else, there are some parenthesis to separate.
    else:
        # We only need to consider the open parentheses.
        pos = [i for i, char in enumerate(paren_string) if char == '(']
        # The first index in the pos list is the beginning of the first group.
        # And the last index in the pos list is the end of the last group.
        first_group_start = 0
        last_group_end = pos[-1]
        groups = []
        for group_start_idx in pos:
            # The current group ends at the last open parenthesis before the next group start.
            group_end_idx = pos[pos.index(group_start_idx) + 1] - 1

            # The slice of the string from the beginning of this group to the end of this group is
            # what we will separate.
            groups.append(paren_string[group_start_idx:group_end_idx + 1])
        return groups

