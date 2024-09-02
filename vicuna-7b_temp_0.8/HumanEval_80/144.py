
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
    # Create a dictionary to store the distinct letters
    # Initialize it with all letters as distinct
    distinct_letters = set(string.ascii_uppercase)

    # Iterate through the string s
    for i in range(len(s)):
        # Get the substring from index i to index i+2
        substring = s[i:i+3]

        # Check if the length of the substring is at least 3
        if len(substring) < 3:
            return False

        # Check if every 3 consecutive letters are distinct
        for j in range(1, len(substring)):
            if substring[j-1] in distinct_letters and substring[j] == distinct_letters.pop():
                distinct_letters.add(substring[j-2])
            else:
                distinct_letters.add(substring[j-1])

        # Reset the dictionary of distinct letters if needed
        if len(distinct_letters) == 0:
            distinct_letters = set(string.ascii_uppercase)

    return True