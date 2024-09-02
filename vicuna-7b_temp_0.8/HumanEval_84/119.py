
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
    if N < 2 or N > 10000:
        return "0"
    
    while N:
        if N % 2 == 0:
            N = N // 2
            continue
        elif N % 5 == 0:
            N = N // 5
            continue
        else:
            N = N // 3
            if N > 10000:
                break
    
    res = "1"
    for i in range(len(str(N))):
        res += str(N % 10)
    return res