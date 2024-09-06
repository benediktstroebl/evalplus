
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
        if n == 0:
            return 1
        return n * factorial(n - 1)

    def sum_until(n):
        return (n * (n + 1)) // 2

    return [sum_until(n) if n % 2 else factorial(n) for n in range(1, n + 1)]

