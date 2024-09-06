from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, Closer in zip('(()') + s + '())':
        stack = [0]
        level = 0
        while opener in Closer:
            stack.append(level)
            if opener == Closer:
                break
            level += 1
        result.append(stack.pop())
    return result