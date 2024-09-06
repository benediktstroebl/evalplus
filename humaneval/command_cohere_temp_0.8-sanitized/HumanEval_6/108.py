from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()') + s + '())':
        level = int(str(opener == closer))
        result.append(max(0, max(result) if result else 0 + level))
    return result