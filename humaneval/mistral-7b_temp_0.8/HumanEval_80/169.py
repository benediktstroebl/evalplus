
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
    s = list(s)
    #  we check if the string is happy by checking if the lenght of the string is at least 3
    if len(s) < 3:
        return False
    # then we use a for loop to iterate through the list of characters in the string
    # and we check if the difference between the indexes of the consecutive characters is equal to 3
    # if it is, we check if the characters at the indexes are distinct
    # if they are, we return True
    # if not, we return False
    for i in range(0, len(s) - 2):
        if s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i + 2] != s[i]:
            return True
        else:
            return False

