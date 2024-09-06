
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # def yield_digits(n):
    #     while n:
    #         yield n % 10
    #         n = n // 10

    # def is_even_digit(digit):
    #     return digit % 2 == 0

    # def yield_between(n, m):
    #     if n <= m:
    #         for x in range(n, m + 1):
    #             yield x
    #     else:
    #         for x in range(n, m - 1, -1):
    #             yield x

    # return list(
    #     map(
    #         lambda n: n * 10 ** i + d,
    #         yield_between(
    #             int(''.join(map(str, filter(is_even_digit, yield_digits(a))))),
    #             int(''.join(map(str, filter(is_even_digit, yield_digits(b)))))))
    #     for i in range(a.bit_length(), b.bit_length())
    #     for d in range(0, 10, 2))

    # def yield_digits(n):
    #     while n:
    #         yield n % 10
    #         n = n // 10

    # def is_even_digit(digit):
    #     return digit % 2 == 0

    # def yield_between(n, m):
    #     if n <= m:
    #         for x in range(n, m + 1):
    #             yield x
    #     else:
    #         for x in range(n, m - 1, -1):
    #             yield x

    # return list(
    #     int(''.join(map(str, filter(is_even_digit, yield_digits(n))))))
    # for i in range(a.bit_length(), b.bit_length())
    # for d in range(0, 10, 2))

    # def yield_digits(n):
    #     while n:
    #         yield n
