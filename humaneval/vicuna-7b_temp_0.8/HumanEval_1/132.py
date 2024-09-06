from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_chars(string, char):
        """Counts the number of occurrences of a given character in a string"""
        return string.count(char)

    def count_parens(string, level=0) -> int:
        """Recursively counts the number of opening parentheses in a string"""
        if not string:
            return level
        level += count_chars(string, '(') - count_chars(string, ')')
        return count_parens(string[1:], level) + count_chars(string, ')')

    def scan_string(string):
        """Scans a string and returns the number of opening parentheses"""
        count = 0
        current_level = 0
        for char in string:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
                if current_level == 0:
                    count += 1
        return count

    def get_open_parens(string, level=0) -> List[int]:
        """Returns a list of the positions of opening parentheses in the string"""
        open_parens = []
        for i in range(len(string)):
            if string[i] == '(':
                open_parens.append(i)
            elif string[i] == ')':
                if open_parens:
                    open_parens[-1] = min(open_parens[-1], i - open_parens[-1])
                open_parens.append(i)
        return open_parens

    string = paren_string.strip('()')
    if not string:
        return []

    open_parens = get_open_parens(string)
    if not open_parens:
        return []

    closed_parens = [string[i:j] for i, j in zip(open_parens, open_parens[1:]) if j - i >= 0]
    closed_parens = [f'{string[i]:<20}{c}{string[j]:>20}' for i, c, j in zip
