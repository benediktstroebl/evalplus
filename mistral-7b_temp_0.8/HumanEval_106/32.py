
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    if n%2 == 0:
        fact = 1
        for i in range(1,n+1,2):
            fact *= i
        return [fact for _ in range(n)]
    else:
        sum = 0
        for i in range(1,n+1,2):
            sum += i
        return [sum for _ in range(n)]
