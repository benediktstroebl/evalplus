from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group)) if group else [0]) ) for group in s.split(' ')]