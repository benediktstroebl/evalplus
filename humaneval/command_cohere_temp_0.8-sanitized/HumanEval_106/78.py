def f(n):
    """ Return a list of size n such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    """
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result
def factorial(n):
    """ Returns the factorial of n which is the multiplication of the numbers from 1 to n (1 * 2 * ... * n).
    """
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)