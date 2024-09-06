
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
    binary = []
    while N > 0:
        if N % 2 == 0:
            binary.append('0')
        else:
            binary.append('1')
        N //= 2
    return ''.join(binary)

    # Convert number to binary representation
    # Loop from right to left
    # If the number is even, append 0
    # Otherwise, append 1
    # Join the binary representation

