
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
    def count_map(s):
        count = {}
        for i, c in enumerate(s):
            if c not in count:
                count[c] = 0
            count[c] += 1
            if i >= 3:
                count[s[i - 3]] -= 1
            if i >= 2:
                count[s[i - 2]] -= 1
            if i >= 1:
                count[s[i - 1]] -= 1
        return count

    def check_count_map(count_map):
        for k in count_map.keys():
            if count_map[k] > 0:
                return False
        return True

    count_map = count_map(s)
    return check_count_map(count_map)
