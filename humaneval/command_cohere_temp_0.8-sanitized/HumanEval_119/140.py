def match_parens(lst):
    def check(s, paren_count):
        if not s:
            return True
        if s[-1] == '(':
            return paren_count > 0 and check(s[:-1], paren_count + 1)
        return check(s[:-1], paren_count)

    return 'Yes' if any(check(s, paren_count) for s, paren_count in zip(lst, range(len(lst[0]) + 1))) else 'No'