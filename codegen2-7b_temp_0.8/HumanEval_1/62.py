from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    count = 0
    index_of_start_paren = 0
    list_of_strings: List[str] = []
    for index_of_end_paren in range(len(paren_string)):
        if paren_string[index_of_end_paren] == ")":
            count += 1
        if count == 0:
            list_of_strings.append(paren_string[index_of_start_paren:index_of_end_paren])
            index_of_start_paren = index_of_end_paren + 1
    
