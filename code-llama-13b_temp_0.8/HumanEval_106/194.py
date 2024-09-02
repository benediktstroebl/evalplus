
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    def next_factorial(n):
        if n == 0:
            return 1
        return n * next_factorial(n-1)

    res = []
    for i in range(n):
        if i % 2 == 0:
            res.append(next_factorial(i))
        else:
            res.append(sum(range(i+1)))
    return res

