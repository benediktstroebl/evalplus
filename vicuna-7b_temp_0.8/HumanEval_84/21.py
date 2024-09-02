
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
    # convert N to binary
    N_bin = str(N).zfill(16)

    # check if N is a power of 2
    if N % 2 == 0:
        # if N is a power of 2, the leftmost 1 is the first digit
        digit = N // 2
        # add the leftmost digit to the output
        output = f"{N_bin[0]}1"
        # if N is not a power of 2, it must have at least one leftmost 0
        # so we add 10000000000000000000000 to the output
        if len(N_bin) > 1:
            output += "100000000000000000000000"

    else:
        # if N is not a power of 2, we need to check each digit
        # if the digit is 0, we add 1 to the output
        digit = 0
        while N % 2 == 0:
            if N % 2 == 1:
                digit = 1
                N //= 2
            N %= 2
        # if the digit is 1, we add 1 to the output
        if digit == 1:
            digit = 0
            while N % 2 == 1:
                digit += 1
                N //= 2
        # add the digit to the output
        output = f"{N_bin[0]}1{digit}0000000000000000000000"

    return output
