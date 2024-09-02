
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
    if N <= 1:
        return "0"
    elif N <= 2:
        return str(N)
    elif N <= 21:
        return str(N) + "000000000000000"[::-1]
    else:
        temp_sum = 0
        for i in range(N):
            temp_sum += int(str(i)[2:])
        return str(temp_sum) + "1"
