
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    # write your answer between #start and #end
    #start
    i = 1
    ans = []
    while i<=n:
        if i%2 == 0:
            ans.append(math.factorial(i))
        else:
            sum1 = 0
            for j in range(1, i+1):
                sum1 += j
            ans.append(sum1)
        i += 1
    return ans
    #end
