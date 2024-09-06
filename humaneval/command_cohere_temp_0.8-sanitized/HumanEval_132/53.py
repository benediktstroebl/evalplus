def is_nested(s):
    stack = []
    brackets = {'[': ']', '(': ')', '{': '}'}
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            top = stack.pop() if stack else '#'
            if brackets[top] != brackets[char]:
                return False
        else:
            return False
    return not stack