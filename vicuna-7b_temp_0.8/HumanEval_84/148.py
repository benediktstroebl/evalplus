
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
    # convert N to binary
    N = str(N)
    binary = "0"
    count = 0
    for digit in N:
        if digit == '0':
            count += 1
        else:
            count = 10
            binary += str(count)
    # check if N is greater than 10
    if N > 10:
        # append 0 to the right side of binary number
        binary += "0" * (N - 10)
    # convert binary number to string
    binary_str = binary[::-1]
    # return the binary number
    return binary_str
