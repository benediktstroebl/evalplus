
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    digit_len = n
    two_digit_len = n + 1

    start_one_count = 0
    end_one_count = 0

    while two_digit_len > 0:
        start_one_count += 10 ** (digit_len - 2)
        end_one_count += 10 ** (digit_len - 2)

        two_digit_len -= 2

    return start_one_count + end_one_count

