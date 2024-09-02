
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = a.lower()
    b = b.lower()
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] == a[i]:
                if i == 0 or j == 0:
                    continue
                for k in range(len(a) - i):
                    for l in range(len(b) - j):
                        if a[i:i+k] in b[j:j+l] or a[i:i+k] == b[j:j+l].lower():
                            return True
    return False

c = "cdefghi"
d = "hjklm"
