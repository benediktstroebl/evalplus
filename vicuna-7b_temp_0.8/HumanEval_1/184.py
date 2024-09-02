from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_braces(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def count_balanced(s):
        stack = []
        count = 0
        for char in s:
            if char == '(':
                stack.append(char)
                count += 1
            elif char == ')':
                if not stack:
                    return count * 2
                stack.pop()
                count -= 1
            elif char == ' ':
                pass
            else:
                count -= 1
        return count

    def parse_group(s):
        count = count_open_braces(s)
        if count == 0:
            return '()'
        else:
            return ')'

    def parse_string(s):
        balanced_count = count_balanced(s)
        return ')' * balanced_count

    def parse_group_string(s):
        count = count_open_braces(s)
        if count == 0:
            return '()'
        else:
            return ')'

    open_braces = 0
    paren_groups = []
    for char in paren_string:
        if char == '(':
            open_braces += 1
        elif char == ')':
            open_braces -= 1
        elif open_braces == 0:
            if len(paren_string) - char_index >= 2:
                next_open_brace = paren_string[char_index:char_index+2]
                if next_open_brace == '):':
                    paren_groups.append(paren_string[char_index+2:])
                    char_index += 3
            else:
                paren_groups.append(paren_string[char_index:])
                char_index += 1
        else:
            paren_groups.append(paren_string[char_index:])
            char_index += 1
    
