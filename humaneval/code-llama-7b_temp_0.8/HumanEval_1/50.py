from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def find_matching_paren(paren_list: List[str], start_idx: int, start_char: str) -> str:
        """ Find the matching closing parentheses, then return the substring with balanced parentheses.
        The function returns the substring where there are no unmatched parentheses within the substring.
        >>> find_matching_paren(['(', ')', '(', ')', '(', ')'], 1, '(')
        '()'
        """
        paren_count = 1  # Keep a running tally of how many parentheses we are inside of
        end_idx = None

        for idx in range(start_idx, len(paren_list)):
            if paren_list[idx] == start_char:
                paren_count += 1
            elif paren_list[idx] == ')':
                paren_count -= 1

            if paren_count == 0:
                end_idx = idx
                break

        return ''.join(paren_list[start_idx:end_idx + 1])

    # Separate the input string into a list of individual characters
    paren_list = [c for c in paren_string if c != ' ']

    # Recursively separate the parentheses
    solution: List[str] = []

    while paren_list:
        # Base case: no more parentheses to process
        if not paren_list:
            break

        # Find the first opening brace
        for idx in range(len(paren_list)):
            if paren_list[idx] == '(':
                break

        # If no opening brace, the string is not balanced
        if paren_list[idx] != '(':
            raise ValueError('Input parentheses are not balanced.')

        # Find the matching closing brace, then remove it from the list
        substring = find_matching_paren(paren_list, idx, '(')
        solution.append(substring)
        for _ in range(len(substring)):
            paren_list.pop(idx)

    return solution

