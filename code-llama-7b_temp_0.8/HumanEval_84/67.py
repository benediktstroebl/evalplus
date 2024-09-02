
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
    
    # sanity checks
    if N is None or N <= 0 or N > 10000:
        raise Exception("Invalid input")
    
    # convert the number to binary
    binary_num = bin(N)[2:]

    # sum the digits in the binary number
    result = 0
    for i in range(0, len(binary_num)):
        result += int(binary_num[i])

    # return the result in binary
    return bin(result)[2:]

