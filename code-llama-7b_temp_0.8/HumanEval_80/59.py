
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
    # We can use a for loop to check if it is happy
    # If it is not happy, it will return false
    # If it is, it will return true

    # We can also make a list and add the letters to the list
    # Then we can see if the letters are distinct
    # If they are, it will return true
    # If not, it will return false

    if len(s) < 3:
        return False

    # We can also use the set function
    # This makes all items unique and only shows one of each item

    # Set is usually used for removing duplicate items
    # or to find unique items

    if len(s) > 3:
        s_list = []

        for letter in s:
            s_list.append(letter)

        if len(s_list) < 3:
            return False

        # We can use the set function to make it so only
        # unique items are in the set
        s_set = set(s_list)

        # Then we can compare the number of items in the
        # set to the number of items in the list
        # If they are equal, they are all unique and we can
        # return true. If not, we can return false
        if len(s_set) == len(s_list):
            return True
        else:
            return False
