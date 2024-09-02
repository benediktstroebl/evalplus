
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
    # Convert N to binary
    binary = str(N)
    # Initialize variable
    result = ""
    # Iterate over each digit of binary number
    for i, digit in enumerate(binary):
        # If current digit is 0, continue to next digit
        if digit == "0":
            continue
        # Append current digit to result
        result += str(digit)
    # Return result
    return result
