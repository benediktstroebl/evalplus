from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Steps:
    # 1. Deal with the edge case: If no paren string is provided, return an empty list
    # 2. Initialize an empty list of results
    # 3. Iterate through the paren string, character by character.
    # 4. Deal with the edge case: If there are no more characters to read, return the results list
    # 5. If we have a left brace, append it to a stack
    # 6. If we have a right brace, pop the stack and append it to a list of results
    # 7. If the character is anything other than a left or right brace, append it to a string
    # 8. If we have a non-empty stack, append the remaining stack to the results list
    # 9. Return the results list
    if not paren_string:
        return []

    results = []
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                results.append(stack.pop() + char)
            else:
                results.append(char)
        else:
            if stack:
                results[-1] += char
            else:
                results.append(char)
    return [result for result in results if result]

