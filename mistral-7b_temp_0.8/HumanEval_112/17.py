
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
    #the reverse delete is done by subtraction
    #then I made a list of all the characters that need to be deleted
    #then I looped through the string to check if the characters are in the list and deleted them
    #then I made a list of all the characters left and checked if it's a palindrome
    #and returned the string and whether it's a palindrome or not
    #For the palindrome part, I used a while loop
    #the loop starts by comparing the first and last character
    #if they're not equal, then the while loop starts
    #the while loop will start by comparing the first and last character
    #if they're not equal, then the loop starts
    #the loop will loop until the first and last character are equal
    #I used the index() method to check if the character is in the list
    #If it's not in the list, then the loop will continue
    #If it's in the list, then the loop will break
    #If the loop breaks, then the while loop will break
    #If the while loop breaks, then the loop will
