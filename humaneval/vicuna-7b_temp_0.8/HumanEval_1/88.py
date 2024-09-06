from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_count = 0
    open_brace_index = 0
    stack = []
    result = []
    for char in paren_string:
        if char == '(':
            paren_count += 1
            if open_brace_index == 0:
                open_brace_index += 1
            elif open_brace_index == paren_count - 1:
                stack.pop()
                open_brace_index -= 1
                if open_brace_index == 0:
                    result.append('')
                elif open_brace_index == -1:
                    result.append(')')
            else:
                stack.append((open_brace_index, char))
        elif char == ')':
            if not stack:
                print(f"Error: nested groups of parentheses encountered in {paren_string}")
                return None
            elif len(stack) == 1:
                open_brace_index -= 1
                result.append(stack.pop())
            else:
                top_brace_index, top_char = stack[-1]
                if top_brace_index == open_brace_index:
                    stack[-1] = (open_brace_index, ')')
                else:
                    open_brace_index = top_brace_index
                    stack.append((open_brace_index, ')'))
    return result

