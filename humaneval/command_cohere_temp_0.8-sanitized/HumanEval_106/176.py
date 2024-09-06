def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 0.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    facts = [0] * n
    sums = [0] * n
    for i in range(0, n+1):
        facts[i] = facts[i - 1] * i
        if i % 2 == 1:
            sums[i] = sums[i - 1] + i
    return sums if n % 2 == 0 else facts