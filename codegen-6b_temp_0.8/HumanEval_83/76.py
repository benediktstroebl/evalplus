
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # if the n is less than or equal to 0 then there is no valid number
    if n <= 0:
        return 0

    # count the number of valid n-digit integers that start with 1 and end with 1
    count = 0
    for i in range(10**(n-1), 10**n):
        # if the first digit is 1 then increment the count
        if i // 10**(n-1) % 10 == 1:
            count += 1

        # if the last digit is 1 then increment the count
        if i % 10**n % 10 == 1:
            count += 1

    return count

