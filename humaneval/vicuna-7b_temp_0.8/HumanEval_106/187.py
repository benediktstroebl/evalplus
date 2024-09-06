
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    n = min(n, 1000)
    result = [0] * n
    for i in range(n, 0, -1):
        if i % 2 == 0:
            result[i] = i * i
        else:
            result[i] = sum(result[j] * i for j in range(1, i))
    return result