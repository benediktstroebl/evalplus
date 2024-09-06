
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #first lets find the length of the bigger string
    bigger_string = a if len(a)> len(b) else b
    shorter_string = a if len(a)< len(b) else b

    #lets get all the rotations of the bigger string
    rotated_strings = list()
    i = 0
    while i < len(bigger_string):
        rotated_strings.append(bigger_string[i:] + bigger_string[:i])
        i+=1
    #now check if the smaller string is in the rotated list
    for string in rotated_strings:
        if shorter_string in string:
            return True
    return False
