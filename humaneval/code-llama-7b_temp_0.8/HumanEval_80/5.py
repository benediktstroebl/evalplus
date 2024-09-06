
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

    def generate_hash(string):
        hash_table = dict()
        for char in string:
            if char not in hash_table:
                hash_table[char] = 1
            else:
                hash_table[char] += 1
        return hash_table

    string = s
    if len(string) < 3:
        return False
    hash_table = generate_hash(string)
    for key in hash_table:
        if hash_table[key] > 1:
            return False
    return True

