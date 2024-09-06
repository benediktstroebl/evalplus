from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        chunk = chunk.replace('(', '')
        chunk = chunk.replace(')', '')
        depth = len(chunk) if chunk != '' else 0
        result.append(depth)
    return result