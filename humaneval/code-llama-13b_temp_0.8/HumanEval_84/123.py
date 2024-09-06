
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
    
    assert isinstance(N, int), 'N is not an integer'
    assert N >= 0 and N <= 10000, 'N is out of range [0, 10000]'
    
    binary_number = str(bin(N))[2:]
    sum_of_digits = sum([int(c) for c in binary_number])
    return bin(sum_of_digits)[2:]

