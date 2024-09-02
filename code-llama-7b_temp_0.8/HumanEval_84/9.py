
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
    # assert that N is an integer
    assert type(N) == int
    # assert that N is between 0 and 10000
    assert N >= 0 and N <= 10000

    bin_number = bin(N)[2:]
    # this is to get rid of the first 0b in the binary number
    binary_sum = 0
    for i in bin_number:
        binary_sum += int(i)
    return binary_sum

