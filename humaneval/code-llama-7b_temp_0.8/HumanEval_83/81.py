
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    s = set()
    # a loop to add numbers that end with 1
    for i in range(1, 10**(n-1)+1):
        x = str(i)
        if x[0] == "1" and x[-1] == "1":
            s.add(i)
    # add numbers that start with 1
    s.add(1)
    for i in range(1, 10**(n-1)+1):
        x = str(i)
        if x[0] == "1":
            s.add(10**(n-1)+i)
    return len(s)
