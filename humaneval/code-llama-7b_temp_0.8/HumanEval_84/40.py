
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
    # Divide by 2, and keep track of remainder
    total = ""
    while N > 0:
        # Get last digit
        # Divide by 2
        # Convert digit to binary
        last_digit = N % 2
        N = N // 2
        total = str(last_digit) + total

    return total
