
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
    # We have a 1 bit in each power, and need to do N / 2 operations.
    steps = N // 2
    remainder = N % 2
    output = ""
    for i in range(steps):
        output += "1"
        output += "0"
    if remainder:
        output += "1"
    return output

