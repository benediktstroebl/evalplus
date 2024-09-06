
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Sort n-digit integers from smallest to largest
    n_digit_ints = [int("1" + "0" * (n - 1))]
    for i in xrange(n - 1, 0, -1):
        n_digit_ints.append(n_digit_ints[-1] * 10)
    n_digit_ints = sorted(n_digit_ints)

    # Count the unique starting and ending numbers
    return sum(1 for _, start, end in n_digit_ints if start == 1) * sum(1 for _, start, end in n_digit_ints if end == 1)

