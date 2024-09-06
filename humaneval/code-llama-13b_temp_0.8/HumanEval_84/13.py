
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
    # --- init
    result = []
    # --- conver N into binary
    binary_N = bin(N)
    # --- getting rid of '0b' at the begining
    binary_N = binary_N[2:]
    for n in range(len(binary_N)):
        result.append(int(binary_N[n]))
    # --- sum up
    total = sum(result)
    # --- result
    return bin(total)
