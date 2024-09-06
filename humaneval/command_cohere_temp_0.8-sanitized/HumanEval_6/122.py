from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = [1]
        sum_of_open = 0
        for char in segment:
            if char == '(':
                sum_of_open += 1
            else:
                open_brackets.append(sum_of_open)
                sum_of_open -= 1
        result.append(max(open_brackets))
    return result