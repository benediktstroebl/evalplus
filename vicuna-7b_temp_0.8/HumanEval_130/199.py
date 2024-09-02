
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
    # [1, 1, 1, ...]
    x1, x2, x3 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    x1[0] = 1
    for i in range(1, n + 1):
        x1[i] = (x1[i - 1] + x2[i - 1] + x3[i - 1]) % 10
        x2[i] = (x2[i - 1] + x3[i - 1] + x1[i]) % 10
        x3[i] = x1[i] + x2[i] + x3[i - 1]

    return x1[:n + 1]