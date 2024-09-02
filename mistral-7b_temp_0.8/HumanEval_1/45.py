from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def find_balanced_group(string: str) -> str:
        """ This function will find a string of nested parentheses and return it
        The function assumes that the outermost parenthesis is open parentheses
        """
        start_bracket = '('
        end_bracket = ')'

        i = 0
        current_bracket_count = 0
        output_string = ''
        while i < len(string):
            bracket_char = string[i]
            if bracket_char == start_bracket:
                current_bracket_count += 1
            elif bracket_char == end_bracket:
                if current_bracket_count == 0:
                    return output_string
                current_bracket_count -= 1
            output_string += bracket_char
            i += 1
        raise ValueError('unable to parse string ' + string)

    output_strings = []
    index = 0
    while index < len(paren_string):
        next_index = find_balanced_group(paren_
