
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
    # we create a new string and a counter
    # we go through all letters in s
    # if letter is not in c, we add it to our new string
    # we return the tuple with our new string and a condition that checks if it is palindrome
    s1=""
    counter=0
    for letter in s:
        if letter not in c:
            s1 += letter
        else:
            counter+=1
    return s1, s1[::-1] == s1 and counter!=len(s)

