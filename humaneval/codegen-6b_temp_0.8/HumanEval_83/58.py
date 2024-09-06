
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def check_start_end(n_digit_numbers):
        if n_digit_numbers[0] == 1 or n_digit_numbers[-1] == 1:
            return 1
        return 0

    def get_n_digit_numbers():
        if n > 1:
            yield from get_n_digit_numbers()
        yield n

    return sum(check_start_end(d) for d in get_n_digit_numbers())
