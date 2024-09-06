import re
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses."""
    patterns = s.split()
    res = []
    for p in patterns:
        level = re.findall(r'\([^()]*\)', p)
        res.append(len(level))
    return res