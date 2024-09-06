from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parens = '( )'
    open_braces = '('
    closed_braces = ')'
    open_braces_stack = []
    closed_braces_stack = []
    paren_strings = []
    paren_index = 0
    brace_index = 0
    pop_open_braces = False

    paren_strings.append('')
    for i in range(len(paren_string)):
        if paren_string[i] in parens:
            paren_strings[paren_index] += paren_string[i]
            brace_index = i
        elif paren_string[i] == open_braces:
            open_braces_stack.append(brace_index)
            pop_open_braces = True
            brace_index = i
        elif paren_string[i] == closed_braces:
            closed_braces_stack.append(brace_index)
            pop_open_braces = False
            brace_index = i
        elif not pop_open_braces:
            paren_strings[paren_index] += paren_string[i]

        if len(open_braces_stack) == len(closed_braces_stack):
            if open_braces_stack:
                paren_strings.append('')
                paren_index += 1

            paren_strings[paren_index] += paren_string[open_braces_stack[-1]+1:closed_braces_stack[-1]]
    return paren_strings

