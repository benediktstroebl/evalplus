
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    list_1 = []
    for i in range(1, n+1):
        if i%2 == 0:
            list_1.append(factorial(i))
        else:
            list_1.append(sum_from_one_to_i(i))
    return list_1
