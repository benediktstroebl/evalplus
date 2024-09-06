from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, Closer in zip('(()') + s + '())':
        stack = [0]
        balance = 0
        while opener != Closer:
            if opener == '(':
                stack.append(balance)
                balance += 1
            else:
                balance -= 1
                stack.append(balance)
        result.append(max(stack))
    return result