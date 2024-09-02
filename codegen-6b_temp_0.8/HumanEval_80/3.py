
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
    else:
        first_letter = s[0]
        second_letter = s[1]
        third_letter = s[2]
        if (second_letter == first_letter) and (third_letter == second_letter):
            return False
        if (second_letter == third_letter) and (first_letter == second_letter):
            return False
        if (first_letter != second_letter != third_letter) and (first_letter != second_letter):
            return False
        return is_happy(s[1:])
    