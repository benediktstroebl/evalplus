
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # variable to keep track of the current index
    i = 1
    # variable to keep track of the current value
    value = 1
    # the list to store the final result
    result = []
    # loop through the n elements
    for j in range(n):
        # check if the current index is even
        if i % 2 == 0:
            # set the value of the element at the current index
            result[j] = value
            # update the value
            value = value * i
        else:
            # add the value of the element at the current index to the result
            result.append(value)
            # update the value
            value = value + i
    return result