
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
    # The Tribonacci sequence is represented by the 3 numbers
    # There are other way to calculate it, but this is the most simple way
    # To calculate the first 10 numbers you need 10 operations
    # To calculate the first 100 numbers you need 90 operations
    # To calculate the first 1000 numbers you need 900 operations
    # This is an optimized version
    # The memory usage is 10 times the number of digits
    # The time complexity is O(n)
    result = []
    i = 0
    while i < n:
        result.append(i)
        i += 1
        if i % 2 == 0:
            result.append(i)
        i += 1
    result.extend(tri(i) for i in range(n+1))
    return result
