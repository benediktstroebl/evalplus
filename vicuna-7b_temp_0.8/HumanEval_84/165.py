
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
    # binary representation of N
    binary = str(N)

    # converting binary to decimal
    decimal = 0
    for i in binary:
        decimal = decimal * 2**int(i)

    # sum of digits
    sum = 0
    for i in range(len(decimal)):
        sum += int(decimal[i])

    # converting decimal to binary
    binary = str(sum)

    # return the output
    return binary
