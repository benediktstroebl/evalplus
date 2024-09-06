
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    def multiply(x, y):
        return x * y

    def odd_numbers(n):
        return filter(lambda x: x % 2 == 1, str(n))

    def is_odd(n):
        return n % 2 == 1

    def digit_product(n):
        return reduce(multiply, odd_numbers(n))

    if is_odd(n):
        return digit_product(n)
    else:
        return 0

