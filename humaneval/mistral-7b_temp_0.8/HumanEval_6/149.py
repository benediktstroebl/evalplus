from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def compute_levels_of_nesting(paren_string: str) -> int:
        """ Helper function to compute the nesting level of the first and last bracket of the input.
        Nesting level is the number of sub-brackets inside a bracket.
        E.g. (() has nesting level of 1.
        Note that this is similar to the number of sub-brackets if we were counting brackets in a string.
        E.g. (()) has nesting level of 2.
        """
        bracket_level = 0
        for char in paren_string:
            if char == '(':
                bracket_level += 1
            elif char == ')':
                bracket_level -= 1
            if bracket_level < 0:
                raise ValueError(f'Malformed input: "{paren_string}"')
        return bracket_level

    # Implement the outer function here
    # Loop through the string by spaces
    # Parse the sub-strings by parentheses
    # Then compute the nest
