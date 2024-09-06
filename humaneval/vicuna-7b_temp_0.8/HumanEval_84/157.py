
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
    # Initialize the binary string with 0s
    result = "0"
    current_sum = 0
    for i in range(N):
        result = "1" + result
        current_sum += int(N % 10)
        N = N // 10
    # Add the current digit sum to the result
    result = "0" + str(current_sum) + result
    return result
