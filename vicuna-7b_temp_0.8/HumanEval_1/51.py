from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def nest_count(s: str) -> int:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return -1
        return count
    
    def nest_max(s: str, max_nest: int) -> int:
        nest = 0
        for char in s:
            if char == '(':
                nest += 1
            elif char == ')':
                nest -= 1
                if nest < 0:
                    return -1
        return max(nest, max_nest)
    
    def parse_nested_list(s: str) -> List[str]:
        stack = []
        open_parens = 0
        nest_max = nest_max(s, 0)
        for char in s:
            if char == '(':
                open_parens += 1
            elif char == ')':
                open_parens -= 1
                if open_parens == 0:
                    stack.append(s[nest_max:])
                    open_parens = nest_max + 1
                elif nest_max - open_parens < 0:
                    return []
            elif char == ' ':
                nest_max = nest_max(s, nest_max)
            elif char in '):':
                if not nest_count(s):
                    return []
                nest_max = nest_max(s, nest_max)
        if not nest_count(s):
            return []
        return stack
    
    return parse_nested_list(paren_string)

