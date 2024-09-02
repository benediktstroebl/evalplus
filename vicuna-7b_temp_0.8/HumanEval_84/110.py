
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
    # Check if N is a positive integer less than 10000
    if N < 10000:
        return str(N)
    
    # Convert N to a binary string
    binary = str(N)
    
    # Initialize sum to zero
    sum = 0
    
    # Iterate over each digit of binary string
    for i in range(len(binary)):
        # If binary string is not zero, add the value of current digit to sum
        if binary[i] == '1':
            sum += int(binary[i])
    
    # Return the sum of digits in binary form
    return sum
