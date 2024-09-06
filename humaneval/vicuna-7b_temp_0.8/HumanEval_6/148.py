from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = []
    for opening, closing in zip(re.finditer(r'\((.+?)\)(.+?)\s*\(', paren_string), re.finditer(r'\)\s*([^()]+\)', paren_string)):
        opening_idx, closing_idx = opening.start(), closing.start()
        opening_count = count.pop(opening_idx)
        closing_count = count.pop(closing_idx)
        count.append(opening_count + 1)
    return count