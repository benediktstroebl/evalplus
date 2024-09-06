from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_group_levels = []
    for group in paren_string.split():
        group_levels = []
        start = 0
        while True:
            match = re.search(r"\(([^()]+)\)", group[start:])
            if match is None:
                break

            group_levels.append(len(match.group(1)) + 1)  # we add 1 because we want to count the innermost parenthesis
            start += match.start(1)

        nested_group_levels.append(max(group_levels) if group_levels else 0)

    return nested_group_levels

