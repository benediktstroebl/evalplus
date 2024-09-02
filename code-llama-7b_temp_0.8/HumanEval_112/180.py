
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
    # Step 1: check if s is palindrome
    # Step 2: iterate over s, if any character is not in c, then we add it to a new string
    new_string = ""
    for letter in s:
        if letter not in c:
            new_string = new_string + letter

    # Step 3: check if new_string is palindrome
    # Step 4: if yes, we return True
    # Step 5: if no, we return False
    new_string_reverse = ""
    for letter in new_string:
        new_string_reverse = letter + new_string_reverse
    
    if new_string == new_string_reverse:
        return (new_string,True)
    else:
        return (new_string,False)


