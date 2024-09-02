
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    counter = 0
    for i in range(1, n + 1):
        num_one = 0
        count = 0
        for j in range(len(str(i))):
            if str(i)[j] == '1':
                num_one += 1
            if num_one == 3:
                break
            count += 1
        if count == i:
            counter += 1
    return counter

