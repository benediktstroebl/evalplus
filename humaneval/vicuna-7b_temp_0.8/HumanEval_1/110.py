from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def count_open_brace(s: str) -> int:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def balance(s: str) -> str:
        opening_brace_count = count_open_brace(s)
        closing_brace_count = opening_brace_count
        result = []
        for i in range(len(s)):
            if s[i] == '(':
                opening_brace_count -= 1
                if opening_brace_count < 0:
                    closing_brace_count += 1
            elif s[i] == ')':
                closing_brace_count += 1
                if closing_brace_count > opening_brace_count:
                    result.append(s[i:])
                    opening_brace_count = opening_brace_count
                    closing_brace_count = closing_brace_count
                    i += 1
                else:
                    result.append(s[i:i+2])
                    i += 2
        if result:
            result.append(s[i:])
        return result

    def match_and_separate(s: str) -> str:
        left = ''
        right = ''
        for i in range(len(s)):
            if s[i] == '(':
                left = s[i+1:i+2]
                i += 2
            elif s[i-1] == ')':
                right = s[i-2:]
                i -= 2
            elif s[i] == ')':
                result.append(left)
                left = right
                right = s[i+1:]
            else:
                result.append(s[i])
        result.append(right)
        return result

    result = balance(paren_string)
    return match_and_separate(result)
