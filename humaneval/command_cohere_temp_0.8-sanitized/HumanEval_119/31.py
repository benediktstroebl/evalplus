def match_parens(lst):
    def merge(a, b):
        stack = []
        for c in a + b:
            if c == '(':
                stack.append(c)
            else:
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack
    
    return 'Yes' if merge(lst[0], lst[1]) else 'No'