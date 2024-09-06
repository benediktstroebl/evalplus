
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # edge case
    if len(a) < len(b):
        return False
    # find and reverse b
    reversed_b = b[::-1]
    # concatenate a with reversed b
    concat_ab = a + reversed_b
    # get length of ab
    concat_len = len(concat_ab)
    # get number of repetitions of b in a
    num_repetitions = concat_len // len(b)
    # get max number of repetitions in a
    max_reps = concat_len // len(a)
    # get length of a
    len_a = len(a)

    # for each repetition
    for rep in range(1, max_reps + 1):
        # get the index to start slicing from
        start_index = (rep - 1) * len_a
        # get the end index
        end_index = start_index + len_a
        # slice a
        sliced_a = concat_ab[start_index:end_index]
        # check if b == sliced_a
        if sliced_a == b:
            # return True
            return True

    return False
