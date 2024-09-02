
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    # initialize the array
    # for this problem, the index starts from 1.
    return_array = [0] * (n + 1)

    # loop through the array
    for i in range(1, n + 1):

        # if i is even
        if i % 2 == 0:

            # factorial of the number
            factorial = 1

            # loop through the number until the factorial
            for j in range(1, i + 1):
                factorial *= j

            # update the array with the factorial
            return_array[i] = factorial

        # if i is odd
        else:

            # the sum of the numbers from 1 to i
            sum = 0

            # loop through the number
            for j in range(1, i + 1):

                # add the number to the sum
                sum += j

            # update the array with the sum
            return_array[i] = sum

    # return the array
    return return_array

