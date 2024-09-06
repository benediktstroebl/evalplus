from typing import List
def parse_nested_parens(paren_string: str) -> List[int]:
    return [max(1 + depth, deepest) for deepest, depth in enumerate(collections.Counter(paren_string).values()) if depth >= 1]