
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
    """
    The problem can be solved in O(n) complexity.
    First note that the value tri(0) and tri(1) are constants and are known.
    Second note that for tri(2) we have the formula tri(2) = 1 + (2 / 2) = 2, so we 
    can calculate it.
    Third note that we can calculate tri(3) by using the formula tri(3) = tri(2) + tri(1) + tri(4).
    If we notice that tri(4) is a constant, we can calculate it. So the problem can be solved 
    in O(1) time.
    So if we can calculate tri(n) for all n from 2 to 4 by using the formula tri(n) = tri(n - 1) + 
    tri(n - 2) + tri(n + 1), we will be done.
    """
    tri_numbers = [3, 1]
    n = 4
    while n < n+1:
        tri_numbers.append(tri_numbers[n-
