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
    return '[' in stack and ']' in stack and stack.index('[') < stack.index(']')
