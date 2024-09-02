
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
    # Convert to a list
    s = list(s)
    # Current index
    i = 0
    # Hashset of characters
    seen = set()
    # Set of characters to skip
    skip = {s[0], s[1]}

    # Loop through the list
    while i < len(s):
        # If the character is in the skip set, skip it
        if s[i] in skip:
            i += 1
            continue

        # If the character has been seen, return false
        if s[i] in seen:
            return False

        # Add to seen set
        seen.add(s[i])

        # If it is the end of the string, return True
        if i == len(s) - 1:
            return True

        # Move to the next character
        i += 1

        # If the character is the last character, return true
        if i == len(s) - 1:
            return True

        # If the next character is the same as the previous, return false
        if s[i] == s[i - 1]:
            return False

        # Add the next character to the skip set
        skip.add(s[i])

    return True
