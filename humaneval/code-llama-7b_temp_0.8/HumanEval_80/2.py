
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

    # SOLUTION 1:
    # For each 3 consecutive letters in the string, check if they are distinct

    # if len(s) < 3:
    #     return False
    # for i in range(len(s) - 2):
    #     if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
    #         return False
    # return True

    # SOLUTION 2:
    # Use a list to store the three letters

    # if len(s) < 3:
    #     return False
    # count = 3
    # while count <= len(s) - 1:
    #     if s[count - 2] == s[count - 1] or s[count - 2] == s[count] or s[count - 1] == s[count]:
    #         return False
    #     count += 1
    # return True

    # SOLUTION 3:
    # Convert string to a list using list() and check if all the elements are different

    # if len(s) < 3:
    #     return False
    # return len(set(s[i : i + 3]) for i in range(0, len(s) - 2, 3)) == len(s) // 3

    # SOLUTION 4:
    # Use a dictionary to count the number of occurences of each letter

    if len(s) < 3:
        return False
    letters = {}
    for letter in s:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return len(letters.values()) == len(s) // 3
