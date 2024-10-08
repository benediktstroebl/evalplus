
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # list of length n
    # f(n) = [1] if n is 0
    # f(n) = [1, 1] if n is 1
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    else:
        return f(n - 1) + [f(n - 1)[-1] + x for x in f(n - 1)]

