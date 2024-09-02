
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
    result = ""
    for i in range(base_case):
        if N > 0:
            if (N % 10) == 0:
                result += str(N // 10)
            if (N % 10) == 1:
                result += "1"
            if (N % 10) == 2:
                result += "10"
            if (N % 10) == 3:
                result += "100"
            if (N % 10) == 4:
                result += "1000"
            if (N % 10) == 5:
                result += "10000"
    return result