
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #remove the characters from the word that are not in the pattern
    #rearrange the pattern so that it is in the alphabetical order
    #for every character in the word, look for it in the pattern. if it is not there then it is not a substring
    #if it is found then check for the rest of the characters in the word
    #if any character in the word is not found in the pattern then it is not a substring
    #if any character in the pattern is not found in the word then it is not a substring

    #approach
    #remove the characters from the word that are not in the pattern
    #rearrange the pattern so that it is in the alphabetical order
    #for every character in the word, look for it in the pattern. if it is not there then it is not a substring
    #if it is found then check for the rest of the characters in the word
    #if any character in the word is not found in the pattern then it is not a substring
    #if any character in the pattern is not found in the word then it is not a substring
    #
