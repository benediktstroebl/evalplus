
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
    # ==========================================
    # Method 1.
    # ==========================================
    # # Convert integer to string
    # s = str(N)
    # # Convert string to binary
    # binary_s = s.encode('utf-8').decode('utf-8')
    # # Split binary_s
    # b = [int(i) for i in str(binary_s)]
    # return str(sum(b))

    # ==========================================
    # Method 2.
    # ==========================================
    # Convert integer to binary
    return bin(N)[2:].split('0')[0].replace('1', '10')
