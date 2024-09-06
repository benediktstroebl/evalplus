
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # The function will return the list of size n, with the values
    # of the elements as described in the problem statement
    # We use a dictionary to store the values, where the keys are the
    # indices, and the values are the values
    values = {i: i! for i in range(n)}

    # We use a list to store the elements of the list
    result = []

    # We iterate over the range of indices from 1 to n, and for each index
    # we check whether it is even or odd, and we add the corresponding value
    # to the result list
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(values[i])
        else:
            result.append(sum(values[j] for j in range(1, i+1)))

    return result