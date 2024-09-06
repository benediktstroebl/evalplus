from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        cnt = 0
        for j, c in enumerate(char):
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                result.append(j)
                break
        if cnt > 0:
            result.append(i)
    return result