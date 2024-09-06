
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
    # the first digit is the rightmost digit
    if N % 2 == 0:
        digit = '0'
    else:
        digit = '1'

    # if N is even, we can multiply by 2 and use the same digit
    if N // 2 == 0:
        N = 2 * N
        digit = '0'

    # add the current digit to the result
    result += digit

    # multiply by 10 and subtract the previous result if necessary
    for i in range(1, N - 1):
        result = '0' + result
        if N % i == 0:
            if i % 2 == 0:
                N = N // i
                result = '0' + result
            else:
                N = N // i + 1
        else:
            N = N // i

    return result

