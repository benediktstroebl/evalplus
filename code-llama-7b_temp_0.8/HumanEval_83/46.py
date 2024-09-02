
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start_one = []
    end_one = []
    for i in range(1, 10**(n-1)):
        start_one.append(str(i).zfill(n))
        end_one.append(str(i).zfill(n))
    start_one.append('1' + '0' * (n-1))
    end_one.append('1' + '0' * (n-1))
    return len(start_one) + len(end_one)

