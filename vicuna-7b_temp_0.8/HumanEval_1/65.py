from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_parentheses(string) -> int:
        count = 0
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def count_nested_parentheses(string, nesting_level=0) -> int:
        count = 0
        for char in string:
            if char == '(':
                count += 1
                nesting_level += 1
            elif char == ')':
                count -= 1
                nesting_level -= 1
                if nesting_level == 0:
                    count -= 1
        return count

    def group_open_parentheses(nesting_level, string, result=None) -> List[str]:
        if result is None:
            result = []
        if nesting_level == 0:
            result.append(string)
        for char in string:
            if char == '(':
                nesting_level += 1
                result_group = group_open_parentheses(nesting_level, string, result)
                result = result_group + [string]
                nesting_level -= 1
            elif char == ')':
                nesting_level -= 1
        return result

    string = paren_string.replace(')', '')
    string = string.replace('(', '')
    string = ''.join(filter(str.isdigit, string))
    result = group_open_parentheses(0, string)
    return result
