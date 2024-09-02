
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
    # Create a set to store the distinct letters
    # Add each letter of the string to the set once
    set_of_letters = set()
    for letter in s:
        set_of_letters.add(letter)

    # Check if the length of the string is at least 3
    if len(s) < 3:
        return False

    # Check every 3 consecutive letters in the string
    for i in range(1, len(s)):
        # If the length of the substring is not a multiple of 3,
        # then the substring is not distinct and the function returns False
        if i + 3 < len(s) and s[i:i + 3] == s[i + 3:i + 6]:
            return False
        # Otherwise, the function continues with the next check

    # If the function reaches here, it means that all 3-consecutive substrings are distinct,
    # which means that the string is happy
    return True