from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if char == '(':
            nesting = 1
            while i < len(s) and s[i] == '(':
                i += 1
                nesting += 1
            result.append(nesting)
        elif char == ')':
            nesting -= 1
            if nesting < 0:
                result.append(0)
                break
            result.append(nesting)
    return result