from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # paren_stack = []
    # result = []
    # # 괄호 쌍이 맞지 않으면 에러를 발생시키는 함수
    # def raise_error():
    #     raise ValueError('Parentheses are not balanced')
    #
    # for paren in paren_string:
    #     if paren == '(':
    #         paren_stack.append(paren)
    #     elif paren == ')':
    #         if not paren_stack:
    #             raise_error()
    #         else:
    #             paren_stack.pop()
    #             if not paren_stack:
    #                 result.append('')
    #     else:
    #         if not paren_stack:
    #             result.append(paren)
    #         else:
    #             result[-1] += paren
    #
    # if paren_stack:
    #     raise_error()
    # return result
    stack = []
    res = []
    for paren in paren_string:
        if paren == '(':
            stack.append(paren)
        elif paren == ')':
            if len(stack) == 0:
                res.append('')
            elif stack.pop() == '(':
                res[-1] += paren
            else:
                raise ValueError('Parentheses are not balanced')
        else:
            if stack:
                res[-1] += paren
            else:
                res.append(paren)
    return res

