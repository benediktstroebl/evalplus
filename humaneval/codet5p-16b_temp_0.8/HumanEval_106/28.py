
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    
    
    def factorial(i):
        fact = 1
        for n in range(1, i+1):
            fact *= n
        return fact
    
    def sum_of_range(i):
        return i * (i + 1) / 2
    
    return [factorial(i) if i % 2 == 0 else sum_of_range(i) for i in range(1, n+1)]
    
    
