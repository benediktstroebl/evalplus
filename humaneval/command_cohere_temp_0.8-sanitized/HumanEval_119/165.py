def match_parens(lst):
    def shift_brackets(brackets):
        stack = []
        for char in brackets:
            if char == '(':
                stack.append(char)
            else:
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack

    return "Yes" if shift_brackets(lst[0]) and shift_brackets(lst[1]) else "No"