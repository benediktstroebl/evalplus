
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
    if len(s) < 3:
        return False
    current_config = s[0:]
    next_config = s[1:]

    # This loop checks for consecutive appearances of the same letter
    while len(current_config) >= 3:
        for i in range(len(current_config) - 1):
            if current_config[i] == current_config[i + 1]:
                return False
        current_config = next_config
        next_config = ""
        for j in range(len(current_config) - 1):
            next_config = next_config + current_config[j]

    # The last three letters are not consecutive and
    # even if we do not check for the last three,
    # we still need to check the middle of the string
    for k in range(len(s) - 3):
        if s[k] == s[k + 1] == s[k + 2]:
            return False

    return True

