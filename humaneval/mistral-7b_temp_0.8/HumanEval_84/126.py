
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
    # The result list
    res = []
    # Take the length of the input to iterate the string
    for i in range(len(str(N))):
        # Take the current digit
        digit = N % 10
        # Convert the digit into binary
        res.append(bin(digit)[2:])
        N = N // 10
    # Return the result list in reverse order
    return ''.join(res[::-1])

