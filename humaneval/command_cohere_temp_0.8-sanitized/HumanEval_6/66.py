from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        cnt = 0
        j = i
        for c in char:
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                result.append(cnt)
                j += cnt
                cnt = 0
        if cnt > 0:
            result.append(cnt)
        i = j + 1
    return result