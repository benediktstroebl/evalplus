from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        chunk = chunk.strip()
        if not chunk:
            continue
        open_count = chunk.count('(')
        close_count = chunk.count(')')
        result.append(open_count - close_count)
    return result