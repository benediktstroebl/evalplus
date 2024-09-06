
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    import numpy as np

    if n < 2:
        return [1] * n
    else:
        output = f(n-1) * n
        if len(output) == 1:
            output *= 2
        elif len(output) == 2:
            output[0:1] *= 3
        else:
            output[0:2] *= 2

    return output

