from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse_paren_group(paren_group: str) -> int:
        """ parse_paren_group returns the deepest level of nesting of parentheses
        """
        counter = 0
        max_counter = 0
        for paren in paren_group:
            if paren == '(':
                counter += 1
                if counter > max_counter:
                    max_counter = counter
            elif paren == ')':
                counter -= 1

        return max_counter

    return [parse_paren_group(paren_group) for paren_group in paren_string.split(' ')]

