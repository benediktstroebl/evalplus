
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    stack = []
    for i in s:
        if i == "a":
            stack.append("a")
        elif i == "b":
            stack.append("b")
            if stack.count("a") == 2 and stack.count("b") == 1:
                return False
        else:
            stack.pop()
            stack.append(i)
    if len(stack) == 1:
        return True
    return False
