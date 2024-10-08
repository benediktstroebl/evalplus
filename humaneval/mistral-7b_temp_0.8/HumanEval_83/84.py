
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num_one_start = 0
    num_one_end = 0

    for i in range(10**(n-1), 10**n):
        if str(i)[0] == "1" or str(i)[-1] == "1":
            num_one_start += 1
            num_one_end += 1
        elif str(i)[0] == "1" or str(i)[-1] == "1":
            num_one_start += 1

    return num_one_start + num_one_end
