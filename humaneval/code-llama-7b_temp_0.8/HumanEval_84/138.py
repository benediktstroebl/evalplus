
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
    result = 0
    while N > 0:
        # step 1: check if odd or even
        if N % 2 == 0:
            # even
            result += 1
            # print("even")
        else:
            # odd
            result += 1
            # print("odd")
        # step 2: get the next number
        N = N / 2
        # print(N)
    # print(result)
    # step 3: convert to binary
    return bin(result)[2:]


