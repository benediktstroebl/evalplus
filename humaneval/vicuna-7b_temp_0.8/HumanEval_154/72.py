
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    return set(b.split()) - set(a.split())
\end{code}

Here, the function uses the `set` data type to store the words in each string, and uses the set difference operator to find the words that are not in the first string. Then it checks if any of the rotations of the second word are a substring in the first string.

You can use the `cycpattern_check` function in your code like this: