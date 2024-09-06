from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_balanced(s: str) -> int:
        count = 0
        for i, c in enumerate(s):
            if c == '(' or c == ')':
                count += 1
            elif c == ' ':
                count += (len(s) - i) * 2
            elif c == c[::-1]:
                count -= 1
        return count

    def flatten_balanced(s: str) -> str:
        return ''.join(s for i, c in enumerate(s) if c != '(' and c != ')')

    def balance(s: str, i: int) -> str:
        if i == 0:
            return s
        if s[i - 1] == '(':
            j = s.find(')', i - 1) + 1
            if j == i - 1 or s[j] != ')':
                return balance(s, i - 2)
            else:
                return balance(s, j)
        elif s[i - 1] == ')':
            j = s.find('(', i - 1) - 1
            if j == i - 1 or s[j] != '(':
                return balance(s, i - 1)
            else:
                return balance(s, j + 1)
        else:
            return s

    # Performing Counting and Flattening
    left_paren_count = count_balanced(paren_string)
    left_paren_group = flatten_balanced(paren_string)
    right_paren_count = count_balanced(left_paren_group)
    right_paren_group = balance(left_paren_group, right_paren_count)
    return right_paren_group
