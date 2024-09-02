
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
    
    assert (N >= 0 and N <= 10000), "The input number is out of range"
    assert type(N) == int, "The input is not an integer"
    s = bin(N)[2:]
    binary_sum = int(s, 2)
    return binary_sum
