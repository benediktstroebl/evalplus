
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    # Step 1: reverse s
    rev_s = s[::-1]
    
    # Step 2: reverse c
    rev_c = c[::-1]

    # Step 3: Find all charaters in s that are equal to any character in c
    for i in range(len(rev_c)):
        # Search for the character in rev_s
        idx = rev_s.find(rev_c[i])
        # If it's found
        if idx > -1:
            # Delete the character
            rev_s = rev_s.replace(rev_c[i],'')

    # Step 4: Check if rev_s is palindrome
    if rev_s == rev_s[::-1]:
        return rev_s, True
    else:
        return rev_s, False

