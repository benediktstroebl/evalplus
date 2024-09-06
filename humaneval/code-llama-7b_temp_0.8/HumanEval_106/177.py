
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    return [1] + [i for i in range(3,n+1,2) if i%2==0] + [reduce(lambda x,y:x*y,range(1,i+1)) if i%2 else sum(range(1,i+1)) for i in range(2,n+1)]
