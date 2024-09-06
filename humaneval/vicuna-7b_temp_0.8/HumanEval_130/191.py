
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
    # Initialize an empty list to store the first n + 1 numbers of the Tribonacci sequence
    trib_list = []
    
    # If n is even, we can directly calculate the nth number in the sequence
    if n % 2 == 0:
        trib_list.append(n)
    
    # If n is odd, we have to calculate the nth number in the sequence
    else:
        trib_list.append(tri(n - 1) + tri(n - 2) + tri(n + 1))
    
    # Append the remaining numbers in the sequence to the list
    for i in range(1, n + 1):
        trib_list.append(tri(i - 1) + tri(i - 2) + tri(i + 1))
        
    return trib_list
