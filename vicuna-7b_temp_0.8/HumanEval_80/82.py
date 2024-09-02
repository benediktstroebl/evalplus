
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
    # define the max length of the string
    max_length = len(s)

    # initialize an empty list to store the distinct letters
    distinct_letters = []

    # iterate through the string
    for i in range(max_length):
        # get the current letter
        current_letter = s[i]

        # check if the current letter is in the list of distinct letters
        if current_letter in distinct_letters:
            # if so, remove it from the list of distinct letters
            distinct_letters.remove(current_letter)
        else:
            # if not, add the current letter to the list of distinct letters
            distinct_letters.append(current_letter)

    # check if the list of distinct letters is empty
    return not distinct_letters