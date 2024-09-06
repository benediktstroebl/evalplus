
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
    if N < 1 or N > 10000:
        return "Please input number less than 10000"
    else:
        N = bin(N)
        total = 0
        for i in N:
            if i == '0':
                pass
            elif i == '1':
                total = total + 1
        return str(total)

