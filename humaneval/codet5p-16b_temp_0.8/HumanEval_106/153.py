
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    return list(map(lambda x: int(x), [x * (x + 1) for x in range(1, n)])) if n % 2 == 0 else list(map(lambda x: x + sum([x for x in range(1, n)]), range(1, n)))
