from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def contains_unbalanced_braces(paren_string):
        if not paren_string or not paren_string.isalnum():
            return False
        return paren_string.count('(') != paren_string.count(')')

    def extract_balanced_groups(paren_string, group_list):
        # If there are unbalanced braces, we can't proceed
        if contains_unbalanced_braces(paren_string):
            return
        # Otherwise, pop the first '(' and the last ')'
        start_index, end_index = 0, -1
        for i in range(len(paren_string) - 1, -1, -1):
            if paren_string[i] == ')':
                end_index = i
                break
        if end_index == -1:
            return
        paren_string = paren_string[:start_index] + paren_string[end_index + 1:]
        group_list.append(paren_string[start_index + 1:end_index])
        extract_balanced_groups(paren_string, group_list)

    group_list = []
    extract_balanced_groups(paren_string, group_list)
    return group_list

