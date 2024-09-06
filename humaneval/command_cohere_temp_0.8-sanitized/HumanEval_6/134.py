from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = []
        clos_brackets = []
        stack = []
        for c in segment:
            if c == '(':
                open_brackets.append(len(stack))
                stack.append(c)
            elif c == ')':
                stack.pop()
                clos_brackets.append(len(stack))
        result.append(max(open_brackets + clos_brackets))
    return result