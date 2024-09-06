
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
    if n == 1:
        return [3]
    elif n == 2:
        return [1, 3]
    elif n == 3:
        return [1, 1, 3]
    else:
        results = [0] * (n + 1)
        results[0] = 3
        results[1] = 1
        results[2] = 1
        results[3] = 3
        for i in range(4, n + 1):
            if i % 2 == 0:
                results[i] = results[i - 3] + results[i - 1]
            else:
                results[i] = results[i - 2] + results[i - 1] + results[i - 3]
        return results

