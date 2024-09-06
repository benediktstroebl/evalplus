from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(range(len(x)) + [0]), s.split())))) for _ in range(len(s.split()))]