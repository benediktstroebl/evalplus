
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
    # Create a list of digits from binary
    digits = []
    for char in binary:
        if char == '0':
            digits.append(0)
        else:
            digits.append(1)
    # Initialize a variable i to 0
    i = 0
    # Initialize a variable sum to 0
    sum = 0
    # Loop until i is greater than the number of digits
    while i < len(digits):
        # Add each digit in the list to the sum
        sum += digits[i]
        # Increment i
        i += 1
        # Check if sum has a 1 or 0
        if (sum % 2 == 0):
            # Append a 0 to the sum
            sum += '0'
        else:
            # Append a 1 to the sum
            sum += '1'
    # Return the sum
    return sum
