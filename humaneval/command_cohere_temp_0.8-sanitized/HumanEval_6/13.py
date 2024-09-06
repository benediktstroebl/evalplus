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
            else:
                tally -= 1
                if tally in open_brackets:
                    result.append(tally)
    return result