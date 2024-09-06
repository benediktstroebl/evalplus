from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for tok in s.split():
        nest = 0
        imbalance = 0
        stack = []
        for c in tok:
            if c == '(':
                nest += 1
                imbalance += 1
                stack.append(nest)
            elif c == ')':
                nest -= 1
                imbalance -= 1
                if not stack or stack.pop() != nest:
                    imbalance += 1
        result.append(max(nest, imbalance))
    return result