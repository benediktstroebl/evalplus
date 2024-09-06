from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def get_index(lst: List[int], idx: int):
        """
        Helper function to check if list index is valid
        >>> get_index([1, 2, 3], 3)
        -1
        >>> get_index([1, 2, 3], 1)
        0
        """
        if idx < len(lst):
            return idx
        else:
            return -1

    def get_closing_paren(paren_string: str, paren_count: int, start_index: int = 0) -> int:
        """
        Find the next closing parenthesis after start_index in paren_string. If there is no valid closing brace, return -1
        """
        for index in range(start_index, len(paren_string)):
            if paren_string[index] == ')':
                paren_count += 1
            elif paren_string[index] == '(':
                paren_count -= 1
            if paren_count == 0:
                return index
        return -1

    # If the string has no parentheses, return it
    if paren_string.find('(') == -1:
        return [paren_string]

    # Traverse the string
    paren_list = []
    paren_count = 0
    curr_group = ''
    start_index = 0
    for index in range(len(paren_string)):
        if paren_string[index] == '(':
            paren_count += 1
        elif paren_string[index] == ')':
            paren_count -= 1
        if paren_count == 0 and index != len(paren_string) - 1:
            curr_group = paren_string[start_index:index + 1]
            # If the group is balanced, add it to the list
            if len(curr_group) == 2:
                paren_list.append(curr_group[1])
            else:
                paren_list.append(curr_group)
            start_index = index + 1
    #
