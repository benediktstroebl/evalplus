def match_parens(lst):
    def merge(a, b):
        stack = []
        for ch in a + b:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack or stack.pop() != '(':
                    return False
                else:
                    stack.append(ch)
        return not stack
    
    return 'Yes' if merge(lst[0], lst[1]) else 'No'