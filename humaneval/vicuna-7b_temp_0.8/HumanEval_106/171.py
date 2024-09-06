
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    # f(1) = [1]
    yield 1

    for i in range(2, n+1):
        if i % 2 == 0:
            # f(2k) = 2k
            yield i
        else:
            # f(2k+1) = sum(k=1 to i) of (k\*i)
            for j in range(1, i+1):
                yield j*i
