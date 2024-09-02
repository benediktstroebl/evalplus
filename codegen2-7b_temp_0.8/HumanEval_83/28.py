
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for n_digit_positive_integer in n_digit_positive_integer_generator(n):
        if n_digit_positive_integer[0] == 1 or n_digit_positive_integer[-1] == 1:
            count += 1
