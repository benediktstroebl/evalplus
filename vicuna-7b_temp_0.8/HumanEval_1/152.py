from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_brace(input_string: str) -> int:
        count = 0
        for char in input_string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def nesting_level(open_brace: str) -> int:
        return max(0, len(open_brace) - 1)

    def nesting_levels(input_string: str) -> List[int]:
        levels = []
        for char in input_string:
            if char == '(':
                levels.append(nesting_level(open_brace))
            elif char == ')':
                levels[-1] -= 1
            elif char in '):':
                levels.append(nesting_level(open_brace))
        return levels

    def join_substrings(substrings: List[str]) -> str:
        return ' '.join(substrings)

    def add_pair(pair: str, open_brace: str) -> str:
        return ' '.join(pair[0], open_brace, pair[1])

    input_string = paren_string
    input_string = input_string.replace(')', '()')
    input_string = input_string.replace('(', '')

    open_brace_count = count_open_brace(input_string)
    nesting_levels = nesting_levels(input_string)
    substrings = [open_brace for open_brace in nesting_levels if nesting_level(open_brace) > 0]

    substrings = [add_pair(s, open_brace) for s in substrings if s != '']

    return substrings

result = separate_paren_groups(paren_string)
