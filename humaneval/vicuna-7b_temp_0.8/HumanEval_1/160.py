from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_brace(s: str) -> int:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def get_nested_count(s: str) -> int:
        nested_count = 1
        for char in s:
            if char == '(':
                nested_count += 1
            elif char == ')':
                nested_count -= 1
        return nested_count

    def process_group(group: str) -> str:
        open_brace_count = count_open_brace(group)
        if open_brace_count == 0:
            return group
        else:
            nested_count = get_nested_count(group)
            if nested_count == 0:
                return f'{group}'
            else:
                return f'({group})'

    nested_groups = []
    open_parens = 0
    for char in paren_string:
        if char == '(':
            open_parens += 1
        elif char == ')':
            open_parens -= 1
        elif char == '(' and open_parens == 0:
            nested_groups.append(paren_string[index:index])
            index += len(paren_string[index:index + 1])
        elif char == ')':
            if open_parens == 0:
                nested_groups[-1] += f'({paren_string[index]})'
                index += 1
                open_parens += 1

    nested_groups.append(paren_string[index:index + 1])
    return nested_groups
