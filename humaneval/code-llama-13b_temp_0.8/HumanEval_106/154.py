
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    if n==0:
        return []
    if n==1:
        return [1]
    if n==2:
        return [1,2]
    
    f_n=[]
    f_n.append(1)
    f_n.append(2)
    for i in range(3,n+1):
        if i%2==0:
            f_n.append(f_n[i-2]*i)
        else:
            sum=0
            for j in range(1,i+1):
                sum+=j
            f_n.append(sum)
    return f_n



