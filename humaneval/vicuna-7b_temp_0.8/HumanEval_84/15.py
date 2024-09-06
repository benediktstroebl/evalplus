
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
    max_digit = 1
    total = 0
    
    for N in N:
        while N > 0:
            total = total * 2 + (N % 2)
            N = N // 2
        max_digit = max(max_digit, 2 + (N % 2))
    
    result = "1"
    while max_digit > 0:
        result = result + str((max_digit % 2))
        max_digit = max_digit // 2
    
    return result