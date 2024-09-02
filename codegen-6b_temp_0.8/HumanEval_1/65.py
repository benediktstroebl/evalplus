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
    stack = []
    current_string = ""
    brackets = {')': '(', '}': '{', ']': '['}

    for char in paren_string:
        if char == ' ':
            current_string += char
        elif char == '(' or char == '{' or char == '[':
            current_string += char
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack.pop() != brackets[char]:
                current_string += char
        elif char == '}':
            if len(stack) == 0 or stack.pop() != brackets[char]:
                current_string += char
        elif char == ']':
            if len(stack) == 0 or stack.pop() != brackets[char]:
                current_string += char

    new_result = remove_empty_strings(current_string.split(" "))
    return new_result

