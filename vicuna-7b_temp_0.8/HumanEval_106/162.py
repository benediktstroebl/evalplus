
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # Write a function that takes n as input and returns a list of size n, such that
    # the value of the element at index i is the factorial of i if i is even, or the sum of numbers
    # from 1 to i otherwise.
    # The values of the elements are determined based on the value of the index i.

    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
        else:
            result.append(i + 1)
    return result