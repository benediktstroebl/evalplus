from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_braces(input_string: str) -> int:
        count = 0
        for char in input_string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def count_nested_groups(input_string: str) -> int:
        count = 0
        for i in range(len(input_string)):
            if input_string[i] == '(' and count_open_braces(input_string[i+1:]) > 0:
                count += 1
        return count

    def separate_group(input_string: str, i: int) -> str:
        open_brace = input_string[i]
        closed_brace = input_string[i+1]
        if count_open_braces(input_string[i:]) == 0:
            return input_string[i:i+2]
        else:
            return input_string[i:i+2] + '()'

    def separate_paren_groups(paren_string: str) -> List[str]:
        output_list = []
        i = 0
        while i < len(paren_string):
            if paren_string[i] == '(':
                start_index = i
                while paren_string[i] != ')' and paren_string[i] != '(':
                    i += 1
                end_index = i
                group = paren_string[start_index:end_index+1]
                output_list.append(group)
                i += 1
            else:
                output_list.append(paren_string[i:])
                i += 1
        return output_list

    return separate_paren_groups(paren_string)
