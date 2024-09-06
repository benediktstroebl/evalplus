from typing import List, Dict
def parse_nested_parens(s: str) -> List[int]:
    results = []
    nested = {}
    for idx, char in enumerate(s):
        if char == '(':
            if '(' in nested:
                nested['('][-1] += 1
            else:
                nested[char] = [0, 1]
        else:
            if char in nested:
                nested[char][-1] -= 1
                if nested[char][-1] == 0:
                    results.append(nested[char][0])
                    del nested[char]
            elif char == ' ':
                results.extend(nested.values())
            else:
                raise ValueError(f"Unexpected character {char} at index {idx}")
    if nested:
        raise ValueError("Input string should have been processed completely")
    return results