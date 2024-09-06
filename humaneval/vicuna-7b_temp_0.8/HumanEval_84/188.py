
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
    # Convert N to binary
    binary_N = str(N).zfill(16)
    
    # Initialize the sum variable
    sum = 0
    
    # Iterate through the binary string
    for digit in binary_N:
        # Check if the digit is 0 or 1
        if digit == '0':
            sum = sum * 2 + 0
        elif digit == '1':
            sum = sum * 2 + 1
    
    return sum
