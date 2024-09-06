from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def reconstruct_paren_group(paren_group):
        """ Helper function to reconstruct a group of parentheses from a list of characters. """
        return ''.join(reversed(paren_group))

    def flatten(paren_group):
        """ Helper function to flatten a group of nested parentheses. """
        if not paren_group:
            return []
        else:
            return [paren_group] + flatten(paren_group[1:])

    def recur(paren_string):
        """ Recursive function to separate the groups of parentheses in the input string. """
        if not paren_string:
            return []
        else:
            opening_brace = paren_string.index('{')
            closing_brace = paren_string.index('}')
            paren_group = paren_string[1:opening_brace]
            flattened_paren_group = flatten(reconstruct_paren_group(paren_group))
            for sub_paren_string in flattened_paren_group:
                new_sub_paren_string = ''.join(sub_paren_string)
                if new_sub_paren_string == '':
                    continue
                if new_sub_paren_string.endswith(')'):
                    sub_paren_string = sub_paren_string[:-1]
                    sub_paren_string += reconstruct_paren_group(reconstruct_paren_group(sub_paren_string))
                else:
                    sub_paren_string = sub_paren_string[:-1]
                    sub_paren_string += reconstruct_paren_group(reconstruct_paren_group(reconstruct_paren_group(sub_paren_string)))
                flattened_sub_paren_group = flatten(reconstruct_paren_group(sub_paren_string))
                for sub_sub_paren_string in flattened_sub_paren_group:
                    new_sub_sub_paren_string = ''.join(sub_sub_paren
