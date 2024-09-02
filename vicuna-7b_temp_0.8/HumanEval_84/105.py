
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
    if N <= 128:
        return "0" + "00000000000000000000000000000000"[N // 2]
    if N % 2 == 0:
        return "0" + str(N // 2)
    else:
        sum = N // 2
        while sum >= 128:
            sum -= 1
            if sum == 1:
                return "1"
            else:
                if N % sum == 0:
                    return "1"
                sum //= 2
        return "1"
