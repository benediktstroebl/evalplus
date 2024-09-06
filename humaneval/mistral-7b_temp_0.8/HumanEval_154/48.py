
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    alphabets_list = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
    for i in range(len(a)-1):
        print(i)
        if a[i] == b[i] :
            print("check")
            if a[i+1] != b[i+1] :
                print("check")
                if a[i+1] in alphabets_list:
                    print(b[i+1])
                    if b[i+1] == b[
