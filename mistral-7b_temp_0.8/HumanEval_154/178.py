
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    words = [a,b]
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                rotate_words = rotate_words(words[j])
                if words[i].find(words[j]) != -1 or words[i].find(rotate_words) != -1:
                    return True
    return False
