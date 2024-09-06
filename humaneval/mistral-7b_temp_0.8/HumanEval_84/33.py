
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
    # Initialise the sum
    sum = 0
    # To store the binary number
    res = ""
    while N > 0:
        # Remainder after division is the binary digit
        rem = N % 2
        # Update the sum of binary digits
        sum += rem
        # Check the remainder
        if rem == 1:
            res += "1"
        else:
            res += "0"
        # Update the number
        N = N // 2
    # Convert the sum of binary digits to binary number
    return bin(sum)[2:]
