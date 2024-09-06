
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
    # Let's consider the length of the string
    # If the string is shorter than 3, return False
    if len(s) < 3:
        return False
    # Let's iterate through the string with a while loop
    while len(s) > 2:
        # Let's create an empty string
        new_str = ""
        # Let's iterate through the string with a for loop
        for i in range(len(s) - 2):
            # Let's check if the character at index i is different from the character at index i + 1 and the character at index i + 2
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                # Let's add the character at index i to the new string
                new_str += s[i]
            # Let's check if the length of the new string is less than the length of the original string
            if len(new_str) < len(s):
