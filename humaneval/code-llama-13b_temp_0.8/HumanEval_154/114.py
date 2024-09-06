
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    first = a
    second = b
    second_length = len(second)

    first_length = len(first)

    if first_length < second_length:
        return False

    for i in range(first_length):
        if first[i:i+second_length] == second:
            return True

        elif first[i:i+second_length] == second[second_length - 1] + second[:second_length - 1]:
            return True

        elif first[i:i+second_length] == second[second_length - 2] + second[:second_length - 2]:
            return True

        elif first[i:i+second_length] == second[second_length - 3] + second[:second_length - 3]:
            return True

    return False

