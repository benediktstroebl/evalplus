def match_parens(lst):
    def expand(s, stack):
        if not s:
            return True
        if s[-1] == '(':
            stack.append(s)
            return expand(s[:-1], stack)
        elif s[-1] == ')':
            if not stack or stack.pop()[-1] != '(':
                return False
        return expand(s[:-1], stack)
    
    return 'Yes' if all(map(expand, lst)) else 'No'