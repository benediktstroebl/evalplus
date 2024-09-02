
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
    # variable declaration
    digits = []
    decimal = 0
    power = 1

    # loop to find the digits of N
    for i in range(1, N+1):
        digits.append(i)
        decimal += N // i
        power *= i

    # convert decimal to binary and reverse
    binary = str(decimal)
    binary = binary[::-1]

    # reverse digits in binary string
    binary_reversed = binary[::-1]
    print(binary_reversed)

    return binary_reversed
