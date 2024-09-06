
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
    # Move the raw input into a string
    strN = str(N)
    # Initialize the sum
    sum = 0
    # Iterate through the string
    for n in strN:
        # Add the current value to the sum
        sum += int(n)
    # Return the string of the binary sum
    return bin(sum)[2:]

