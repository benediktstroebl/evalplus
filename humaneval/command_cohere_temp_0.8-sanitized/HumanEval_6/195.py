from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = []
        tally = 0
        for char in segment:
            if char == '(':
                open_brackets.append(tally)
                tally += 1
            elif char == ')':
                tally -= 1
                if tally == 0:
                    result.append(max(open_brackets))
        if tally > 0:
            result.append(tally)
    return result