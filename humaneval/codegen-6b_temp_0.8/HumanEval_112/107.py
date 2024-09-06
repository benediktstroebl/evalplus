
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
    
    # Step 1: Create a new list
    # Step 2: Iterate through the string and fill the list with the characters of the original string
    # Step 3: Then reverse the list
    # Step 4: Iterate through the reversed list and check if the character is in the c string
    # Step 5: Return the result string and a boolean depending on the result

    res = ''
    for i in s:
        if i not in c:
            res += i
    rev_list = list(reversed(res))
    if res == ''.join(rev_list):
        return (res,''),True
    else:
        return (res,''),False

