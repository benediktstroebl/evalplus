from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        nested = 0
        i = 0
        while i < len(opening) or i < len(closing):
            if opening[i] == '(':
                depth += 1
                nested += 1
            elif closing[i] == ')':
                depth -= 1
                if not depth:
                    result.append(nested)
                    nested = 0
            i += 1
    return result