
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
    distinct_letters = set()
    # Iterate over the string
    for char in s:
        # Add the current character to the set of distinct letters
        distinct_letters.add(char)
        # If the length of the set of distinct letters is 3, add the next character to the set
        if len(distinct_letters) == 3:
            distinct_letters.add(s[0]) # add the first character
            distinct_letters.add(s[1]) # add the second character
            distinct_letters.add(s[2]) # add the third character
        # If the length of the set of distinct letters is not 3, remove the current character from the set
        elif len(distinct_letters) > 3:
            distinct_letters.remove(char)
    return len(distinct_letters) >= 3 and distinct_letters == s[0] and distinct_letters == s[1] and distinct_letters == s[2]