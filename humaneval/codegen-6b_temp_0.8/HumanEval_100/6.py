
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
    return [i + 1 for i in range(n)]

assert make_a_pile(3) == [3, 5, 7]
assert make_a_pile(4) == [4, 6, 8]
assert make_a_pile(5) == [5, 7, 9]
assert make_a_pile(6) == [6, 8, 10]
assert make_a_pile(31) == [31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115, 121, 127, 133, 139, 145, 151, 157, 163, 169, 175, 181, 187, 193, 199, 205, 211, 217, 223, 229, 235, 241, 247, 253, 259, 265, 271, 277, 283, 289, 295, 301, 307, 313, 319, 325, 331, 337, 343, 349, 355, 361, 367, 373, 379, 385, 391, 397, 403, 409, 415, 421, 427, 433, 439, 445, 451, 457, 463, 469, 475, 481, 487, 493, 499, 505, 511, 517, 523, 529, 535, 541, 547, 553, 559, 565, 571, 577, 583, 589, 595, 601, 607, 613, 619, 625, 631, 637, 643, 649, 655, 661, 667, 673, 679, 685, 691, 697, 703, 709, 715, 721, 727, 733, 739, 745, 751, 757, 763, 769, 775, 781, 787, 793, 799, 805, 811, 817, 823, 829, 835, 841, 847, 853, 859, 865, 871, 877, 883, 889, 895, 911, 917, 923, 929, 935, 941, 947, 953, 959, 965, 971, 977, 983, 999, 1005, 1011, 1017, 10