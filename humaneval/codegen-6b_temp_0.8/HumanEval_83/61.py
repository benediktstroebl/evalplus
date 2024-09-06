
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    
    num_ones = 0

    for i in range(1, n):
        if i == 1 or i == n:
            num_ones += 1
            continue
        if i % 2 == 1:
            num_ones += int(i % 10 == 1)
        else:
            num_ones += int(i // 10 % 10 == 1)

    return num_ones
