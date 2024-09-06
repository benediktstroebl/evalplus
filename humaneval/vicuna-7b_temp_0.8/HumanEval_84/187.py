
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
    if N > 10000:
        return "10000"
    elif N % 1000 == 0:
        return "1000" + str(N//1000)
    elif N % 100 == 0:
        return "100" + str(N//100)
    elif N % 10 == 0:
        return "10" + str(N//10)
    else:
        return str(N)
