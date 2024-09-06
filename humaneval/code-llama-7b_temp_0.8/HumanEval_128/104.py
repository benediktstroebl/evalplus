
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    def multiply(a, b):
        return a * b

    def sum_magnitudes(a, b):
        return abs(a) + abs(b)

    def is_negative(a):
        return a < 0

    def is_zero(a):
        return a == 0

    def product_signs(arr):
        return reduce(multiply, map(sign, arr), 1)

    def sign(num):
        return 1 if num > 0 else -1 if num < 0 else 0

    def sum_signs(arr):
        return reduce(sum_magnitudes, map(sign, arr), 0)

    if len(arr) == 0:
        return None
    return product_signs(arr) * sum_signs(arr)

