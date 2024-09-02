
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # Check if the input is an integer
    if n < 1:
        return []
    # Initialize the list with the first element of the factorial
    list_ = [n]
    # For each i, if i is even, add the factorial of i to the list, otherwise,
    # add the sum of numbers from 1 to i to the list
    for i in range(2, n+1):
        if i % 2 == 0:
            list_ += f(i)
        else:
            list_ += [i]
    return list_
