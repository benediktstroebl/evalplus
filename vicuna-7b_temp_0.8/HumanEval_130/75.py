
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
    # Define the functions
    def fib(n):
        """
        Compute the Fibonacci sequence up to the given index n.
        """
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    def tri(n):
        """
        Compute the Tribonacci sequence up to the given index n.
        """
        n = n + 1
        yield n
        if n % 2 == 0:
            yield n // 2
            for i in range(n // 2 - 1, -1, -1):
                yield i
        else:
            for i in range(n - 1, -1, -1):
                yield i
            yield n // 2
    
    # Compute the Fibonacci sequence up to n
    fib_seq = fib(n)
    
    # Use the recurrence relation to compute the Tribonacci sequence
    tri_seq = [n]
    for i in range(1, n + 1):
        tri_seq.append(tri_seq[-1] + tri_seq[-2] + tri_seq[-3])
    
    # Combine the Fibonacci and Tribonacci sequences
    result = []
    for i in fib_seq:
        result.extend(tri_seq[i:])
    return result
