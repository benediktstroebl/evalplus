
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
    if N < 0:
        raise ValueError("Sorry, the input value must be a positive integer.")
    if N == 0:
        return "0"

    # shifting all bits to the left
    N = N << 1
    result = 0
    while N > 0:
        result += N % 10
        N //= 10
    return str(bin(result)[2:])

