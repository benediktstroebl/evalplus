def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{{', ')': '('}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys() and stack and stack.pop() == brackets[char]:
            stack.append(char)
        else:
            return False
    return not stack