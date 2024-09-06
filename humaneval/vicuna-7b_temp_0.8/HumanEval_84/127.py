
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
    # Check that N is a positive integer within range
    if N < 1 or N > 10000:
        return "invalid input"
    
    # Initialize the result string
    result_str = "0"
    
    # Convert N to binary and get the number of digits
    num_digits = len(str(N))
    
    # Iterate through the digits of the result string
    for i in range(num_digits):
        # If the current digit is greater than 9, add a leading zero
        if N >= 10**(num_digits-i-1):
            result_str = "0" + result_str + "1"
        else:
            result_str = "1" + result_str
    
    return result_str
