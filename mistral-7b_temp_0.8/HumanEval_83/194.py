
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n_digits = len(str(n))
    total_numbers = 10**(n_digits)
    numbers_starting_with_1 = int(str(total_numbers)[:n_digits])
    numbers_ending_with_1 = total_numbers - int(str(total_numbers)[:n_digits-1])
    return numbers_starting_with_1 + numbers_ending_with_1

