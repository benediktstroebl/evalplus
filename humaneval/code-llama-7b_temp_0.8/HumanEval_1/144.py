from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    """
    def parse(s: str) -> List[str]:
        left = 0
        right = 0
        res = []
        cur_str = ""
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                right += 1
            if right > left:
                res.append(cur_str)
                left = right
                right = 0
                cur_str = ""
            cur_str += ch
        return res
    """

    def parse(s: str) -> List[str]:
        stack = []
        res = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    stack.append(ch)
            if not stack:
                res.append(s[:len(s) - len(res)])
        return res

    return parse(paren_string)

