
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def cycpattern(a,b):
        if b in a:
            return True
        else:
            return False
    
    def cycpattern_generator(word):
        cyc_word = [word]
        cyc_word_len = len(word)
        while(cyc_word_len > 0):
            cyc_word.append(cyc_word[-1][1:])
            cyc_word_len -= 1
        cyc_word.pop(0)
        return cyc_word
    
    cyc_pattern_list_a = cycpattern_generator(a)
    cyc_pattern_list_b = cycpattern_generator(b)
    for x in cyc_pattern_list_b:
        if x in cyc_pattern_list_a:
            return True
        else:
            continue
    return False
