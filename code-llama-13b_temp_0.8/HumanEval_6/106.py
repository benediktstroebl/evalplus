from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return [
        max(
            (
                len(paren_string)
                - sum(
                    (
                        [
                            len(j) + 2 * len(j.strip(ch))
                            for i, ch in enumerate(paren_string)
                            if i < len(paren_string) - 1
                            and ch == "("
                            and j := paren_string[i + 1 :].split(")", 1)[0]
                        ]
                    )
                )
            ),
            0,
        )
        for paren_string in paren_string.split()
    ]

