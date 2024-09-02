
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start_with_one_count = end_with_one_count = 0
    for x in range(10**(n-1), 10**n):
        if x % 10 == 1:
            start_with_one_count += 1
            end_with_one_count += 1
        elif int(str(x)[0]) == 1:
            start_with_one_count += 1
    return start_with_one_count + end_with_one_count
