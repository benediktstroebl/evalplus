
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
    # binary representation
    binary = str(N)
    # sum of digits
    sum = 0
    # loop through digits
    for i in range(len(binary)):
        digit = int(binary[i])
        # add digit to sum
        sum += digit
    # convert sum to binary
    binary_sum = str(sum)
    return binary_sum
