
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # to create list of size n with 1 as first element
    l = [1] * n
    # to calculate factorial of even numbers
    for i in range(0, n, 2):
        l[i] = 1
        for j in range(2, i + 1):
            l[i] *= j
    # to calculate sum of numbers from 1 to i for odd numbers
    for i in range(1, n, 2):
        for j in range(1, i + 1):
            l[i] += j
    return l

