
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
    if s is None:
        return False

    char_map = {}
    for i in range(len(s)):
        if i < 2:
            char_map[s[i]] = 1
            continue

        current_char = s[i]
        previous_two_chars = s[i-2:i+1]

        if current_char in char_map.keys():
            return False
        else:
            char_map[current_char] = 1

        if previous_two_chars in char_map.keys():
            del char_map[previous_two_chars]
        else:
            return False

    return True
