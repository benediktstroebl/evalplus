
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
    # calculate number of digits
    num_digits = N // 10
    
    # check if the number is power of 2
    if N & (N - 1):
        # return 1
        return "1"
    else:
        # calculate sum of digits
        sum = 0
        for i in range(num_digits):
            sum += N % 10
            N //= 10
        return str(sum)