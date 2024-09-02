
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # 0 -> 0
    # 1 -> 1
    # 2 -> 1
    # 3 -> 3
    # 4 -> 2
    # 5 -> 4
    # 6 -> 5
    # 7 -> 6
    # 8 -> 4
    # 9 -> 5
    # 10 -> 6
    # 11 -> 7
    # 12 -> 8
    # 13 -> 9
    # 14 -> 6
    # 15 -> 8
    # 16 -> 5
    # 17 -> 7
    # 18 -> 9
    # 19 -> 6
    # 20 -> 4
    # 21 -> 0
    # 22 -> 8
    # 23 -> 5
    # 24 -> 5
    # 25 -> 1

    s = str(n)
    d = []
    sumd = 0

    for i in s:
        if int(i) % 2 != 0:
            d.append(int(i))

    for j in d:
        sumd += j

    return sumd

