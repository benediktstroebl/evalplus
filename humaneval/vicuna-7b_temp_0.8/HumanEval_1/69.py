from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def parse_list(s):
        open_brace_count = 0
        close_brace_count = 0
        last_brace_index = -1
        result = []
        for i, char in enumerate(s):
            if char == '(':
                open_brace_count += 1
            elif char == ')':
                close_brace_count += 1
                if close_brace_count == open_brace_count:
                    if last_brace_index != -1:
                        result.append(s[last_brace_index:i])
                    last_brace_index = -1
                    open_brace_count = 0
            elif last_brace_index != -1 and open_brace_count == close_brace_count:
                last_brace_index = i
                open_brace_count = 0
            elif last_brace_index == -1 and (
                    char == '(' or char == '[') and (
                        s[i - 1] == ']' or s[i - 1] == ')')):
                last_brace_index = i
                open_brace_count = 1
        if last_brace_index != -1:
            result.append(s[last_brace_index:])
        return result

    nested_list = [parse_list(paren_string)]
    while nested_list:
        current_list = nested_list.pop(0)
        nested_list = [current_list]
        for i, sublist in enumerate(current_list):
            if i > 0:
                if sublist == '':
                    nested_list.pop(i - 1)
                elif sublist[0] == '(' and sublist[-1] == ')':
                    nested_list[i - 1] = sublist[1:-1]
                    nested_list.append(sublist[1:])
                else:
                    nested_list[i - 1] += ' ' + sublist
    return nested_list