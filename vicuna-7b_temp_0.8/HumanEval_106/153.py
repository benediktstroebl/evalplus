
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # initialize an empty list and a variable i
    result = []
    i = 1

    # check if the input n is odd or even
    if n % 2 == 0:
        # iterate over the list and change the value of the element at index i if i is even
        for j in range(n):
            if j % 2 == 0:
                result[j] = f(j)
        return result
    else:
        # if n is odd, we will iterate only over the first n-1 elements
        for j in range(n-1):
            result[j] = f(j)
        result[n-1] = n * (n-1) / 2
        return result
