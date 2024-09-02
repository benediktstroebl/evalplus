
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    pass

assert f(3) == [1, 2, 6]
assert f(5) == [1, 2, 6, 24, 15]
assert f(6) == [1, 2, 6, 24, 15, 120]
assert f(7) == [1, 2, 6, 24, 15, 120, 720]
