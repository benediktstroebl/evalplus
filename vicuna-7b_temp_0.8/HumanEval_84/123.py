
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
    # Create the binary representation of N
    binary = str(N)

    # Initialize a variable to store the running sum
    running = 0

    # Iterate through the binary representation of N
    for digit in binary:
        # Add the value of the current digit to the running sum
        running += int(digit)

    # The final sum is the value of the running sum
    return "".join(str(digit) for digit in reversed(list(reversed(running))))