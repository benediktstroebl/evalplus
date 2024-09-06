
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

    # def recursive_f(n, lst=[]):
    #     if n <= 0:
    #         return lst
    #     if n % 2 == 0:
    #         return recursive_f(n - 1, lst + [factorial(n)])
    #     return recursive_f(n - 1, lst + [sum(range(1, n + 1))])
    # return recursive_f(n)

    def recursive_f(n, lst=[]):
        if n <= 0:
            return lst
        if n % 2 == 0:
            return recursive_f(n - 1, lst + [factorial(n)])
        return recursive_f(n - 1, lst + [sum(range(1, n + 1))])
    return recursive_f(n)

