
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 1:
        raise ValueError("Input value n should be positive.")
    if n == 1:
        return 1

    if n == 2:
        return 1

    max_number_of_digits = len(str(n))
    s = set()
    for digits in range(1, max_number_of_digits + 1):
        for start in range(1, max_number_of_digits - digits + 1):
            end = start + digits - 1
            x = 10 ** start - 1 + 10 ** end
            s.add(x)

    return len(s)

