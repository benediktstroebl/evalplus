def match_parens(lst):
    def shift(s):
        """
        Shifts the string s such that if it represents a valid parenthesis sequence,
        the result will represent the same valid parenthesis sequence but with
        all open parentheses moved to the left side.
        """
        balance = 0
        res = ''
        for ch in s:
            if ch == '(':
                balance += 1
            elif ch == ')':
                balance -= 1
            res += ch if balance == 0 else ')'
        return res

    return 'Yes' if shift(lst[0]) == shift(lst[1]) else 'No'