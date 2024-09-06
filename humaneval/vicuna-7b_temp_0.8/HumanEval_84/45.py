
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
    N_str = str(N)
    while N > 0:
        N_str = N_str[:-1]
        if N % 2 == 0:
            N = N // 2
            N_str = "0" + N_str
        else:
            N = N // 2
            N_str = N_str + "1"
    return N_str

variables = ["N"]
