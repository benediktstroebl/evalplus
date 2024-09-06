
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # Validate input
    if N <= 0 or N > 10000:
        raise ValueError("Input should be a positive integer between 1 and 10000.")
    
    # Convert N to binary
    binary = str(N)
    n = int(binary[:-1])
    
    # Calculate sum of digits
    sum = 0
    for i in range(len(binary)):
        sum += int(binary[i])
    
    # Convert sum to binary and return as a string
    return sum.to_binary()
