
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
    distinct_chars = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                if s[i] == s[j] or s[j] == s[k]:
                    continue
                if s[i] == s[k]:
                    distinct_chars.add(s[i])
                    distinct_chars.add(s[j])
                    distinct_chars.add(s[k])
    return len(distinct_chars) >= 3

input = input().strip()
result = is_happy(input)
