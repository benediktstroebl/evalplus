
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
    #tribonacci[n] = [1,1,2]
    #tribonacci[n] = [1,2,3]
    #tribonacci[n] = [1,3,5]
    #tribonacci[n] = [1,5,8]
    #tribonacci[n] = [1,8,13]
    #tribonacci[n] = [1,13,21]
    #tribonacci[n] = [1,21,34]
    #tribonacci[n] = [1,34,55]
    #tribonacci[n] = [1,55,89]
    #tribonacci[n] = [1,89,144]
    #tribonacci[n] = [1,144,233]
    #tribonacci[n] = [1,233,377]
    #tribonacci[n] = [1,377,610
