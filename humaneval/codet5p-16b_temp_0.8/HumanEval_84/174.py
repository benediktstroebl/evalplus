
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

    import math
    if N < 10:
        return N
    binary = ""
    while N!= 0:
        if N % 2 == 0:
            binary += "0"
        else:
            binary += "1"
        N //= 2
    binary = binary[::-1]
    print(binary)
    return sum([int(binary[i]) for i in range(len(binary))])

