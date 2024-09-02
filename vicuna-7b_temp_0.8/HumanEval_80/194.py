
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
    # Create a dictionary to store the distinct letters of the string
    distinct_letters = {}
    
    # Loop through the string
    for char in s:
        # Check if the letter is in the dictionary
        if char in distinct_letters:
            # If the letter is in the dictionary, update the count for the letter
            if distinct_letters[char] < 3:
                distinct_letters[char] = 1
            else:
                distinct_letters[char] -= 1
        else:
            # If the letter is not in the dictionary, add it with a count of 1
            distinct_letters[char] = 1
    
    # Return True if every 3 consecutive letters are distinct, else return False
    return all(len(distinct_letters[key]) >= 3 for key in set(distinct_letters))
