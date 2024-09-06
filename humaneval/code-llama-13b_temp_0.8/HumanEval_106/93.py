
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    if n == 0:
        return []

    res = [0] * n
    res[0] = 1

    index = 1
    while index < n:
        if index % 2 == 0:
            res[index] = res[index - 1] * index
        else:
            res[index] = sum(range(index + 1))
        index += 1
    return res
