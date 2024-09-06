from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_list = paren_string.split(" ")

    def _recur_parse_nested_parens(paren_string: str, depth: int = 0) -> List[int]:
        paren_string = paren_string.replace(" ", "")
        if depth == 0:
            depth += 1

        if paren_string.startswith("("):
            paren_list = []
            depth += 1
            for i, j in enumerate(paren_string):
                if j == "(":
                    paren_list.append(_recur_parse_nested_parens(paren_string[i + 1:], depth))
                    depth -= 1
                elif j == ")":
                    depth -= 1
                    if depth < 0:
                        break
            return paren_list
        else:
            return [depth]

    return _recur_parse_nested_parens(paren_string)

