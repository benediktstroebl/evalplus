
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # We can use a generator expression to create the sequence of numbers to be included in the list
    numbers = (i for i in range(1, n + 1))
    # We can use a list comprehension to fill the list with the correct values
    return [n // i for i in numbers]