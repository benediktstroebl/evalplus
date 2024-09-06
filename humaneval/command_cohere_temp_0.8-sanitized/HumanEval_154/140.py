def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    return second in set(first) or any(second == s for s in permutations(second))
def permutations(string):
    result = [string[i:] + string[:i] for i in range(len(string))]
    return result