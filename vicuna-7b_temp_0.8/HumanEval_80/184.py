
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
    # Check if the length of the string is at least 3
    if len(s) < 3:
        return False

    # Initialize a dictionary to count the number of distinct letters
    letter_count = {}

    # Iterate through the string
    for char in s:
        # Check if the current letter is in the dictionary and increment the count if it is
        if char in letter_count:
            letter_count[char] += 1
        else:
            # Add the current letter to the dictionary if it's distinct
            letter_count[char] = 1

    # Check if every 3 consecutive letters are distinct
    for i in range(0, len(s), 3):
        # Check if the current three letters are distinct
        if len(set(s[i:i+3])) == 1:
            return True
    return False