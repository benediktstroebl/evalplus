
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
    dp = [0] * 26
    for i in range(len(s)):
        if i % 3 == 0:
            dp[ord(s[i])] += 1
        else:
            dp[ord(s[i])] += 1
        if i == len(s) - 1:
            dp[ord(s[i])] += 1
    return dp[ord("z")] > 0 and dp[ord("z")] == dp[ord("a")] + dp[ord("b")] + dp[ord("c")]