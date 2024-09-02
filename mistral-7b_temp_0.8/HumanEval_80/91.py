
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
    # convert string to list
    lst = list(s)
    # check if length is at least 3
    if len(lst) < 3:
        return False
    # create dictionary to count the occurrence of each letter
    count = {}
    # loop through the string
    for i in lst:
        # if the letter has not been counted yet, count it and add it to the dictionary
        if i not in count:
            count[i] = 1
        # if the letter has been counted before, increment its count
        else:
            count[i] += 1
    # check if any letter has a count greater than 2
    for key in count:
        if count[key] > 2:
            return False
    # if no letter has a count greater than 2, return True
    return True
