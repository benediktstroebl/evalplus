from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if char == '(':
            nesting = 1
            while i < len(s) and nesting > 0:
                if s[i] == '(':
                    nesting += 1
                elif s[i] == ')':
                    nesting -= 1
                i += 1
            result.append(nesting)
    return result