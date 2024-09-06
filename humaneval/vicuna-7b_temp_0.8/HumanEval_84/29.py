
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
    N = int(N)
    sum = 0
    digits = [str(d) for d in map(int, N) if d != 0]
    if N > 0:
        while sum < N:
            sum = sum * 10 + int(digits[-1])
        if sum % 2 == 0:
            return "0" + str(sum / 2)
        else:
            return str(sum / 2)
    else:
        if sum % 2 == 0:
            return "1"
        else:
            return "0"
