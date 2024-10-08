def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(bracket)
    return len(stack) < len(string) and '[' in stack and ']' in stack
