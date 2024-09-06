
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    l=[]
    if n<=0:
        return []
    if n>0:
        i=1
        while i<=n:
            if i%2==0:
                l.append(i**(i/2))
            else:
                t=1
                while t<=i:
                    t=t+1
                    l.append(t)
            i=i+1
    return l
