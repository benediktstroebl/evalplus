from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def find_closest_balanced_group(paren_string):
        opening_paren_counter = 0
        opening_paren_index = 0
        closing_paren_index = 0
        while closing_paren_index < len(paren_string) and opening_paren_counter != 0:
            for i, paren in enumerate(paren_string):
                if paren == '(':
                    opening_paren_counter += 1
                    opening_paren_index = i
                elif paren == ')':
                    opening_paren_counter -= 1
                    closing_paren_index = i
        return opening_paren_index, closing_paren_index

    def find_next_balanced_group(paren_string):
        opening_paren_index, closing_paren_index = find_closest_balanced_group(paren_string)
        if opening_paren_index == len(paren_string):
            return None
        else:
            return paren_string[opening_paren_index:closing_paren_index + 1]
