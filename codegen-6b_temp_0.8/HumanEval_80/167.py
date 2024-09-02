
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
    word_list = [i for i in s if i.isalpha()]
    if len(word_list) < 3:
        return False
    while len(word_list) > 3:
        res = False
        for i in range(1, len(word_list)):
            if word_list[i] == word_list[i - 1]:
                res = True
                break
        if res == False:
            return False
        word_list.pop(0)
        word_list.pop(len(word_list) - 1)
    return True
