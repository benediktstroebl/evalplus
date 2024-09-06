def match_parens(lst):
    def shift_left(stack, char):
        if char == '(':
            stack.append(char)
            return True
        elif char == ')':
            if stack == ['(']:
                return False
            stack.pop()
            if len(stack) == 0:
                return False
            return shift_left(stack, ')')
        else:
            return False

    def is_balanced(stack, char):
        if char == '(':
            return len(stack) >= 1 and stack[-1] == ')'
        elif char == ')':
            return len(stack) >= 1 and stack[-1] == '('
        else:
            return len(stack) == 0

    if len(lst) < 2:
        return 'No'
    stack = []
    for char in lst[0]:
        if not shift_left(stack, char):
            return 'No'
    stack.pop()
    for char in lst[1]:
        if not shift_left(stack, char):
            return 'No'
    return 'Yes' if is_balanced(stack, '') else 'No'