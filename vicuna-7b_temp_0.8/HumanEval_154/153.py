
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if b.isalnum() or b == " ":
        for i in range(len(b)):
            for j in range(i+1, len(b)):
                # convert a and b to lowercase
                a = a.lower()
                b = b.lower()
                rot_a = ""
                for k in range(len(a)):
                    rot_a += a[k] if k+1 < len(a) else " "
                if b in rot_a or b == rot_a[::-1]:
                    return True
        return False
    else:
        return True

a = input()
b = input()
