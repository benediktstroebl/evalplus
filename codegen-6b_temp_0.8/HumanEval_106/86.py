
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    ans = [0 for i in range(n)]
    ans[1] = 1
    for i in range(2,n):
        ans[i] = i * ans[i-1]
    for i in range(n-1,-1,-1):
        if i % 2 == 0:
            ans[i] = ans[i//2] * ans[i] * 2
        else:
            ans[i] = ans[i] + sum(range(n-i,0,-1))
    return ans
