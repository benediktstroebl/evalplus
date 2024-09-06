from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # First step is to convert all input into a list of lists.
    # Parentheses that are separated by spaces are not meant to be grouped
    nested_parens = [
        [i] if i in [")", "("] else i
        for i in paren_string.replace(" ", "").replace("()", "|")
    ]

    # This function will take in a list of strings and return a list of ints representing the
    # deepest nesting level for that set of parentheses.
    def _nesting_depth_recursive(parens: List[str], level: int = 0) -> int:
        nonlocal nested_parens

        if parens == []:
            return level
        elif parens[0] == "(":
            parens.pop(0)
            level += _nesting_depth_recursive(parens, level)
        else:
            parens.pop(0)
            level += _nesting_depth_recursive(parens, level)
        return level

    result =
