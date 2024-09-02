
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
    # Use a dictionary to count the number of distinct letters in the string
    # Initialize the count of distinct letters to 0
    count = 0
    for char in s:
        if char in DISTINCT_LETTERS:
            count += 1
    # If the length of the string is less than 3, it cannot be happy
    if len(s) < 3:
        return False
    # If the count of distinct letters is 0, it cannot be happy
    if count == 0:
        return False
    # If the string has at least 3 characters and every 3 consecutive characters are distinct
    # then it is happy
    for i in range(len(s)-2):
        # If the characters at index i, i+1, and i+2 are distinct,
        # then check if the length of the substring is at least 3
        if len(s[i:i+3]) >= 3 and DISTINCT_LETTERS[s[i]] != DISTINCT_LETTERS[s[i+1]] and DISTINCT_LETTERS[s[i]] != DISTINCT_LETTERS[s[i+2]]:
            # If the length of the substring is at least 3 and the characters are distinct,
            # then the string is happy
            return True
    # If we reach here, then the string cannot be happy
    return False
