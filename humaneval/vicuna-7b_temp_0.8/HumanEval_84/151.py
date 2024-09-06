
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
    # Convert N to binary and store it in binary_form
    binary_form = str(N)

    # Initialize a variable for the sum of digits
    sum_of_digits = 0

    # Loop through each character in the binary_form string
    for ch in binary_form:
        # Add the current digit to the sum of digits
        sum_of_digits = sum_of_digits * 2 + ch

    # Convert the sum of digits to binary and return it as the output
    return str(sum_of_digits)
