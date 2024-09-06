
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
    assert int(N) == N, "\n\nN should be an integer\n"
    assert N > 0 and N < 10000, "\n\nN should be between 0 and 10000\n"
    
    _bin = bin(N)[2:]
    print("bin", _bin)
    _bin = _bin.replace("0", " ")
    print("bin", _bin)
    
    return "".join(_bin)
