from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def count_nesting(s: str) -> int:
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            else:
                count += 1
        return count

    def flatten_list(lst: List[List[int]]) -> List[int]:
        flattened = []
        for i in range(len(lst)):
            for n in lst[i]:
                flattened.extend(n)
        return flattened

    def extract_nesting(lst: List[List[int]]) -> List[int]:
        return lst[0]

    def process_nesting(lst: List[int]) -> List[int]:
        lst = sorted(lst)
        return lst

    def get_nesting(lst: List[List[int]]) -> List[int]:
        return extract_nesting(flatten_list(lst))

    nesting = get_nesting(List(parse_nested_parens(paren_string)))
    return process_nesting(nesting)