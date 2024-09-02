
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
    # The list of numbers we need to store
    sequence = [0, 0, 0]
    
    # If n is odd, use the recurrence relation
    if n % 2 == 1:
        # Calculate the sum of the first two numbers
        first = sequence[0] + sequence[1]
        # Calculate the sum of the first three numbers
        second = first + sequence[2]
        
        # Use the recurrence relation to calculate the next n numbers
        for i in range(n-1, -1, -1):
            sequence[i] = second
            second = first + second
            first = second
    
    # If n is even, use the first n numbers
    else:
        # Calculate the first two numbers
        first = sequence[0] = n
        second = sequence[1] = n/2
        
        # Calculate the next n numbers
        for i in range(2, n+1):
            sequence[i] = second
            second = first + second
            first = second
    
    return sequence
