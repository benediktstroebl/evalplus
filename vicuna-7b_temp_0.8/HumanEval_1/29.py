from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # To avoid ambiguity, we use a dictionary to keep track of the state of the current group of opening and closing
    # brackets, keyed by the string of opening brackets.
    open_brace_state = {}

    def _handle_open_brace(match):
        if match.group() not in open_brace_state:
            open_brace_state[match.group()] = set()  # initialize the set of open brackets if we haven't seen it before
        open_brace_state[match.group()].add(match.group(2))

    def _handle_close_brace(match):
        if match.group() not in open_brace_state:
            return ' '
        open_brace_state[match.group()].remove(match.group(2))
        return ''

    def handle_open_brace(match):
        if match.group() in open_brace_state:
            open_brace_state[match.group()].add(match.group(2))
            return ''
        else:
            return match.group()

    def handle_close_brace(match):
        return handle_open_brace(match)

    def handle_other(match):
        return match.group()

    return re.findall(handle_close_brace, re.sub(handle_open_brace, handle_other, re.sub(handle_close_brace, handle_open_brace, paren_string, 0)))
