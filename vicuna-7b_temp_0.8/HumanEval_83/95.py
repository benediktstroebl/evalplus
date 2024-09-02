
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base case: if n is 1, the answer is 1.
    if n == 1:
        return 1
    # If n is not 1, let's divide it by 10.
    n //= 10
    # Now, let's use a loop to iterate from 1 to n-1 and count the numbers
    # that start or end with 1.
    count = 0
    for i in range(1, n-1):
        # For each number, we check if it starts or ends with 1.
        if n % i == 0 and i == 1 or n % i == 1 and i != 1:
            count += 1
    return count
