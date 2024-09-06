
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
    count_dic = {}
    for char in s:
        count_dic[char] = count_dic.get(char, 0) + 1
    return (3 in count_dic.values() and
            'a' in count_dic and
            'b' in count_dic and
            'c' in count_dic)
