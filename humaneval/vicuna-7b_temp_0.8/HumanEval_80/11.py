
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
    # Find the length of the string s
    n = len(s)
    
    # Create a 2D list to store the frequency of each letter in the string
    counts = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(n+1):
        counts[i][i] = 1
        for j in range(i+1, n+1):
            counts[i][j] = counts[i][j-1]
    
    # Check if the string is happy
    for i in range(3, n+1):
        # Check if all the 3 consecutive letters are distinct
        if all(counts[i-3][j] != counts[i-3][j-1] for j in range(i-2, n+1)):
            return True
    
    return False
