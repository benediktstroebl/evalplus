
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # Start with an empty list
    result = []
    # Iterate over the elements of n
    for i in range(1, n+1):
        # If i is even
        if i % 2 == 0:
            # Add the factorial of i to the result list
            result.append(i * i)
        # Otherwise
        else:
            # Calculate the sum of numbers from 1 to i
            sum = 1
            # Iterate over the numbers from 1 to i
            for j in range(1, i+1):
                sum += j
            # Add the sum to the result list
            result.append(sum)
    return result
