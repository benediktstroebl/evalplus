
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
    # 3 way of generating the sequence
    # 1. using recursion
    # 2. using a list and a index
    # 3. using a dictionary
    if n % 2 == 0:
        result = [3]
        i = 2
        while i <= n:
            result.append(result[i - 1] + result[i])
            i += 1
    else:
        result = []
        j = 1
        while j <= n:
            result.append(result[j - 1] + result[j - 2] + result[j + 1])
            j += 2
    return result