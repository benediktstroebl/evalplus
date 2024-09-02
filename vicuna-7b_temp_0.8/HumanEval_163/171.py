
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return []

    # create a generator that returns the even digits of n
    def even_digits(n):
        # even_digits(10) => [2, 4, 6, 8]
        if n % 2 == 0:
            yield n // 2
        while n > 0:
            n //= 2
            yield n // 2

    # get the first two even digits from the generator
    for digit1, digit2 in zip(even_digits(a), even_digits(b)):
        yield digit1
        yield digit2
