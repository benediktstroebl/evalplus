
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    ans = [n]
    while n > 1:
        if n & 1:
            n += 1
        n >>= 1
        ans.append(n)
    return ans


assert make_a_pile(1) == [1]
assert make_a_pile(2) == [2, 4]
assert make_a_pile(3) == [3, 5, 7]
assert make_a_pile(4) == [4, 8, 12]
assert make_a_pile(5) == [5, 10, 15, 20, 25]
assert make_a_pile(6) == [6, 12, 18, 24, 30, 36]
assert make_a_pile(7) == [7, 14, 21, 28, 35, 42, 49]
assert make_a_pile(8) == [8, 16, 24, 32, 40, 48, 56, 64]
assert make_a_pile(9) == [9, 18, 27, 36, 45, 54, 63, 72, 81]
assert make_a_pile(10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
assert make_a_pile(11) == [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
assert make_a_pile(12) == [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144]
