
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    def factorial(n):
        """the function that calculate the factorial of a given number"""
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        res = [0] * n
        for i in range(n):
            res[i] = factorial(i)
        return res
    else:
        res = [0] * n
        for i in range(n):
            res[i] = factorial(i) + i
        return res

