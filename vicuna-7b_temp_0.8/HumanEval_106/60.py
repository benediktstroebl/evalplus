
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    # the list that will store the values
    values = [0] * n

    # loop through the elements of the list
    for i in range(n):
        # if the current element is even, set it to the factorial
        if i % 2 == 0:
            values[i] = i * values[i - 1]
        # if the current element is odd, set it to the sum of numbers from 1 to i
        else:
            values[i] = sum(range(1, i + 1))

    return values