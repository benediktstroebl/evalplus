
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
    # CHECK IF THE STRING IS 3 OR MORE CHARACTERS IN LENGTH
    if len(s) < 3:
        return False
    # BUILD A LIST FROM THE STRING
    test = list(s)
    # LOOP OVER THE LIST
    for i in range(len(test) - 2):
        # CHECK IF THREE CONSECUTIVE CHARACTERS ARE THE SAME
        if test[i] == test[i + 1] == test[i + 2]:
            return False
    # RETURN THE RESULT
    return True
