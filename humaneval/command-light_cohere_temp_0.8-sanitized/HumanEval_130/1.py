def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence."""
    
    def subsequence(n):
        a = 0
        b = 1
        for _ in range(n):
            c = a + b
            a, b = b, c
        return [c for c in 'abc']

    if n < 1:
        raise ValueError("n should be a positive integer")

    return [subsequence(i) for i in range(1, n+1)]
n = int(input("Enter n: "))