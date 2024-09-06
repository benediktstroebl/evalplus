from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for interval in s.split():
        open, close = interval.count('('), interval.count(')')
        result.append(open - close)
    return result