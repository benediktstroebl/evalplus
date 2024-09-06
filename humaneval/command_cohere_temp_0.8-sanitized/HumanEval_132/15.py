def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{', ']': '['}

    for char in s:
        if char in '][}'[::-1]:  # Look for closing brackets
            stack.append(char)
        else:
            expected_bracket = brackets[char]
            if not stack or stack.pop() != expected_bracket:
                return False
    return not stack