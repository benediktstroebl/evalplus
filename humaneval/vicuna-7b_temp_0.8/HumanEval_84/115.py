
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
    # Initialize variables
    digits = []
    result = 0
    
    # Create a loop to iterate through each digit
    for i in range(N):
        digits.append(str(i))
    result = str(N)
    
    # Remove leading zeroes from digits
    digits = [d for d in digits if d != "0"]
    
    # Remove any leading zeros in result
    result = "0" + result
    
    # Concatenate digits and reverse the order
    result = "".join(reversed(digits))
    
    return result
