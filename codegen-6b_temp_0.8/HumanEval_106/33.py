
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    return []

assert f(1) == [1]
assert f(5) == [1, 2, 6, 24, 15]
assert f(9) == [1, 2, 6, 24, 15, 120, 840, 2520, 120960]
assert f(13) == [1, 2, 6, 24, 15, 120, 840, 2520, 120960, 220640, 676560]
