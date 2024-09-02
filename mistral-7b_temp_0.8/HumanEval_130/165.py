
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    #You can use the same method as for Fibonacci numbers but with 3 instead of 2
    a = 3
    b = 1
    c = 1
    t = 0
    if n == 1:
        return [a]
    elif n == 2:
        return [a,b]
    elif n == 3:
        return [a,b,c]
    else:
        for i in range(n - 3):
            t = a + b + c
            c = b
            b = a
            a = t
        return [a,b,c,t]
    #return tri(n - 1) + tri(n - 2) + tri(n + 1)
