from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    open_brace_count = 0
    current_group = ''
    for char in paren_string:
        if char == '(':
            if current_group == '':
                open_brace_count += 1
            else:
                if open_brace_count > 0:
                    result.append(current_group)
                    current_group = ''
                    open_brace_count -= 1
                current_group += char
        elif char == '}':
            if current_group != '':
                result.append(current_group)
                current_group = ''
            open_brace_count -= 1
    if current_group != '':
        result.append(current_group)
    return result


if __name__ == '__main__':
    # Test the function with a simple case
    assert separate_paren_groups('(()())') == ['()', '(())']

    # Test the function with a more complex case
    assert separate_paren_groups('(()(()))') == ['()', '(()())', '()']
    assert separate_paren_groups('(((()))())') == ['(', '(()())', '())', '()']
    assert separate_paren_groups('(()(((()))))') == ['(', '(()(((())))', '))', '()']