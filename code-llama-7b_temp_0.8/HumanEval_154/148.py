
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #Too simple
    #return a.find(b) != -1 or any(a.find(b+c) != -1 for c in b)

    #Solution 2
    return (b in a) or any(a.find(b+c) != -1 for c in b)



    #Solution 3
    # def check(w1, w2):
    #     return any(w1.find(w2 + w) != -1 for w in w2)
    #
    #
    # def findRotations(str):
    #     rots = []
    #     for i in range(len(str)):
    #         rots.append(str[i:])
    #         if i > 0:
    #             rots.append(str[:i])
    #     return rots
    #
    #
    # def cycpattern_check(a, b):
    #     return (b in a) or any(a.find(b + c) != -1 for c in b)
    #
    # return cycpattern_check(a, b) or any(cycpattern_check(a, b) for b in findRotations(b))

    #Solution 4
    def rotations(s):
        return [s[i:] + s[:i] for i in range(len(s))]


    return a in b or any(a in r for r in rotations(b))

