
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
    # Use a dictionary to keep track of the distinct letters
    distinct_letters = {}

    # Loop through the string and add each letter to the dictionary if it's not already there
    for i in range(len(s)):
        if i % 3 == 0 and s[i] not in distinct_letters:
            distinct_letters[s[i]] = 1

    # If the dictionary contains at least 3 distinct letters, the string is happy
    return len(distinct_letters) >= 3

s = input().strip()
