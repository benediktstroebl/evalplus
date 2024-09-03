from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    return [match.replace('(', m, ')', ')', 1) for m in parentheses]