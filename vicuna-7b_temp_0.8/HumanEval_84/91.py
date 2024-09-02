
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
    # A base case to handle N = 0
    if N == 0:
        return "0"
    # The variable d holds the sum of digits for the current N
    d = 0
    # Iterate through digits of the N
    while N > 0:
        # Add each digit of N to d
        d = d * 10 + N % 10
        # Remove N from the product
        N = N // 10
    # Convert d to binary string
    d_str = str(d)
    return "1" + d_str[1:]
