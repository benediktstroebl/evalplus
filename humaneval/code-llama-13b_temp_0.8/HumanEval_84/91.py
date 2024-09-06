
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
    # time O(log(N)) | space O(1)
    # breakdown: how many times do we have to split N into a remainder and a quotient?
    # since we're going to take the quotient of N and use it for N the answer is how many digits it has.
    # this is equivalent to the number of times we need to divide N by 2.
    # finding the number of digits of a number can be solved in logarithmic time.
    # a number N has log2(N) digits.
    # this is the base 2 logarithm.
    # the logarithm is the inverse function of exponentiation.
    # 4 = 2^2, 8 = 2^3, 16 = 2^4, 32 = 2^5
    # log2(2) = 1
    # log2(4) = 2
    # log2(8) = 3
    # log2(16) = 4
    # log2(32) = 5
    # log2(64) = 6
    # ...
    # log2(1000) = 9.6
    # 9 digits
    
    binary = ''
    while N > 0:
        binary = str(N % 2) + binary
        N //= 2
    return binary
