from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair_str in s.split():
        count = 0
        nested = 0
        opening_bracket = bracket_pair_str[0]
        closing_bracket = opening_bracket[1]
        for char in bracket_pair_str:
            if char == opening_bracket:
                count += 1
            elif char == closing_bracket:
                count -= 1
                if count == 0:
                    nested += 1
        result.append(nested)
    return result