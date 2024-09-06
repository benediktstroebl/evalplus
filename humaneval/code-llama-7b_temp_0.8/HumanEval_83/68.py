
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    first_digit_ones = 9
    last_digit_ones = 1

    # Check if the last digit is one
    while (last_digit_ones * 10) <= n:
        last_digit_ones *= 10

    # Check if the first digit is one
    while (first_digit_ones * 10**(len(str(n)) - 1)) > n:
        first_digit_ones //= 10

    return (n - (first_digit_ones - 1)) // 10 + (last_digit_ones - 1)

