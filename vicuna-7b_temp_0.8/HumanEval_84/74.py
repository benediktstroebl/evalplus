
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
    # Get a list of digits in the binary representation of N
    digits = str(N).split('')
    # Initialize a variable to store the total sum
    sum = 0
    # Iterate over the digits in the list
    for d in digits:
        # Add the current digit to the sum
        sum += d
    # Convert the sum to binary and return it as a string
    return sum.to_binary()
