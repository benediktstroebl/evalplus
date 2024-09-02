
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
    return "".join(str(bin(i)[2:]) for i in range(N))

    # Hint: In Python, bin() function will convert a number to a string of binary representation.
    # Ex: bin(2)[2:]  -> "10"
    #     bin(3)[2:]  -> "11"
    #     bin(4)[2:]  -> "100"
