from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    # Using recursive approach to parse nested parentheses
    def parser(s, l):
        if not s:
            return l
        if s[0] == '(':
            return parser(s[1:], max(l, len(s)-1))
        else:
            return parser(s[1:], l)
    return [parser(group, 0) for group in s.split(' ') if group]