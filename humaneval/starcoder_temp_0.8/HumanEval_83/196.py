
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # build list of possibles
    L = []
    for i in range(1, 10):
        s = str(i)
        L.append(s)
        L.append(s * 9)

    # generate and count possibles
    total = 0
    for i in range(1, 10**n):
        s = str(i)
        if s[0] == '1' or s[-1] == '1':
            total += 1
            continue
        for j in L:
            if s.startswith(j) or s.endswith(j):
                total += 1
                break
    return total
