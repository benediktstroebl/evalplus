
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

    prev_letter = s[0]
    next_letter = s[1]
    counter = 0

    for letter in s:
        if counter == 2:
            if prev_letter == next_letter:
                return False
            prev_letter = next_letter
            next_letter = s[counter + 2]
            counter = 0

        if letter == prev_letter:
            counter += 1
        else:
            counter = 1
        prev_letter = letter

    return True

