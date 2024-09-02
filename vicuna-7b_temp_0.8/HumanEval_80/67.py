
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
    # Define helper function
    def helper(s, index, count=0):
        # Check if we have reached the end of the string
        if index == len(s) - 1:
            # If all distinct characters have been seen, return True
            if count == 3:
                return True
            else:
                return False
        else:
            # If we have seen a repeated character, reset the count
            count = 0
            # Recursively check the rest of the string
            helper(s, index + 1, count)
    # Call helper function
    return helper(s)
