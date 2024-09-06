
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # initialize the list with 1 for each index
    list_of_values = [1] * n
    # iterate through the indices
    for i in range(1, n):
        # check if the current index is even
        if i % 2 == 0:
            # multiply the current value in the list by the factorial of i
            list_of_values[i] = list_of_values[i] * i
        else:
            # add the values of the list up to the current index to the current value in the list
            list_of_values[i] = sum(list_of_values[:i])
    return list_of_values