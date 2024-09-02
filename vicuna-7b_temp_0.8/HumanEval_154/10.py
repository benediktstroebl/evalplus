
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    i=0
    while i<min(len(a),len(b)):
        if a[i:i+len(b)]==b:
            return True
        i+=len(b)
    return False
\end{code}

You can use the `cycpattern_check` function in the following way: