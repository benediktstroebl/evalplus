
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
    digits = [str(d) for d in map(int, N.split())]
    result = 0
    while len(digits) > 0:
        n = int(digits[0])
        digits = digits[1:]
        if n == 0:
            result = result * 2 + 1
        else:
            result = result * 2 + n
    return "".join(str(d) for d in result)
