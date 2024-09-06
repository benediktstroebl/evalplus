
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 0:
        return 0
    
    starts = 0
    ends = 0
    count = 0
    for i in range(1, 10 ** (n - 1)):
        start_digit = str(i)[0]
        end_digit = str(i)[-1]
        if start_digit == '1':
            starts += 1
        if end_digit == '1':
            ends += 1
        if start_digit == '1' or end_digit == '1':
            count += 1

    return starts + ends + count
