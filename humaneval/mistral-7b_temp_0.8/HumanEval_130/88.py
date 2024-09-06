
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
    a = [3]
    b = [3, 1]
    if n == 1:
        return a
    if n == 2:
        return b
    for i in range(2, n):
        a.append(b[i-1] + b[i-2] + b[i-3])
    return a
    """
    a = [3]
    b = [3, 1]
    a.extend(b)
    for i in range(3, n):
        b.append(a[i-1] + a[i-2] + a[i-3])
        a.append(b[i])
    return a
    """


