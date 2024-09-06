
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
    if not isinstance(N, int):
        raise TypeError('N must be a positive integer')
    if N < 0 or N > 10000:
        raise ValueError('N must be a positive integer')
    if N == 0:
        return '0'
    if N == 1:
        return '1'

    binary_number = bin(N)[2:]
    sum = 0
    for bit in binary_number:
        sum += int(bit)
    return bin(sum)[2:]

