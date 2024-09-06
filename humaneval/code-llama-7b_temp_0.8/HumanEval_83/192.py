
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for n1 in range(10**(n-1), 10**n):
        # convert n1 to list
        n1_list = list(str(n1))

        # check if starts or ends with 1
        if n1_list[0] == '1' or n1_list[-1] == '1':
            count += 1
    return count
