
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
    #First, we will iterate through the string s and keep track of all the characters that appear in it
    characters_in_s = set()
    for char in s:
        characters_in_s.add(char)
    
    #Then, we will iterate through the string c and delete all the characters that appear in s
    delete_set = set(c)
    for char in c:
        delete_set.remove(char)
    
    #Finally, we will return the resulting string and check if it's a palindrome
    result_string = ''
    for char in s:
        if char not in delete_set:
            result_string += char
    if result_string == s[::-1]:
        return (result_string, True)
    else:
        return (result_string, False)
