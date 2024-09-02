
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
    # Only positive integers are allowed
    if N < 0 or N > 10000:
        return "Invalid input"
    
    # Convert N to binary and find the sum of digits
    binary = str(N)
    sum = 0
    for digit in binary:
        sum = sum * 2 + digit
    
    # Convert the sum to binary and return the result
    binary = str(sum)
    return binary
