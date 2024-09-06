
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def is_odd(x):
        return x % 2 == 1

    product = lambda x: lambda y: x * y
    reduce = lambda f, s, x: f(s, x)
    digits = lambda n: [int(c) for c in str(n)]
    odds = lambda nums: filter(is_odd, nums)
    products = lambda nums: reduce(product, 1, nums)

    return products(odds(digits(n)))
