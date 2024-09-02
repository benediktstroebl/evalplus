
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
    # Take first digit from binary representation
    digit = int(N)
    
    # Get the number of digits from binary representation
    digits = str(N)[2:].zfill(digits)
    
    # Return the string with first digit added
    return digit + "." + digits

