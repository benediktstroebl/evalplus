
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
    # 用一个列表来存储前3个字母, 如果当前字母和列表中的字母相同，不算happy
    i = 0
    # 用一个列表来存储最后3个字母, 如果这3个字母不是按顺序排列，不算happy
    last_3 = []
    for c in s:
        if i == 3:
            # 如果3个字母都相同，不算happy
            if c == last_3[2]:
                return False
            # 如果3个字母不按顺序排列，不算happy
            if c == last_3[0]:
                return False
        if i == 2:
            last_3.append(c)
        elif i == 1:
            last_3 = [last_3[1], last_3[2], c]
        elif i == 0:
            last_3 = [c, c, c]
        i = (i + 1) % 3
    return len(s) >= 3

