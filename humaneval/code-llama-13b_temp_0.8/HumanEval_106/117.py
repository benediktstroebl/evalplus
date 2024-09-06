
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # your code
    if n == 0:
        return []
    if n == 1:
        return [1]
    result = []
    for i in range(n):
        if i % 2 == 0:
            factorial = 1
            for k in range(1, i + 1):
                factorial *= k
            result.append(factorial)
        else:
            summ = 0
            for k in range(1, i + 1):
                summ += k
            result.append(summ)
    return result
