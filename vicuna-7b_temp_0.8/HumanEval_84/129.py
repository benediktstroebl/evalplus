
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
    # Check if the input is in the range of N ≤ 10000
    if N > 10000:
        return "10000"
    
    # Initialize the sum of digits variable
    sum = 0
    
    # Iterate through each digit of the input N
    for i in range(N):
        sum = sum + (N % 10)
        N = N // 10
    
    # Convert the sum to binary and return it as a string
    binary_sum = str(sum)
    
    # Return the final binary number
    return binary_sum
