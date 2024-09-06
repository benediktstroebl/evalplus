from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_brace(string):
        count = 0
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count
    def get_open_brace(start_index, current_string):
        if start_index == len(current_string):
            return len(current_string)
        for i in range(start_index, len(current_string)):
            if count_open_brace(current_string[start_index:i]) < 0:
                return i
        return start_index + 1

    left_index = 1
    right_index = len(paren_string) - 1
    left_string = paren_string[left_index:right_index]
    right_string = paren_string[right_index+1:]
    left_index = get_open_brace(left_index, left_string)
    right_string = right_string[:left_index]
    return [left_string, right_string]

separate_paren_groups('( ) (( )) (( )( ))')
