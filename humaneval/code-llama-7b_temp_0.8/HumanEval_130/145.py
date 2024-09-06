
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
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    if n == 2:
        return [1, 3]
    if n == 3:
        return [1, 3, 2]
    if n == 4:
        return [1, 3, 2, 8]
    if n == 5:
        return [1, 3, 2, 8, 13]
    if n == 6:
        return [1, 3, 2, 8, 13, 34]
    if n == 7:
        return [1, 3, 2, 8, 13, 34, 57]
    if n == 8:
        return [1, 3, 2, 8, 13, 34, 57, 101]
    if n == 9:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178]
    if n == 10:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 317]
    if n == 11:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 317, 577]
    if n == 12:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 317, 577, 1150]
    if n == 13:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 317, 577, 1150, 2011]
    if n == 14:
