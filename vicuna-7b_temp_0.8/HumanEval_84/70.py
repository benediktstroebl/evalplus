
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
    # convert N to binary and convert each digit to its corresponding ascii character
    binary = str(N).zfill(base)
    digit_string = "".join(map(ord, binary))
    # reverse the order of the digits
    reversed_digits = digit_string[::-1]
    # sum of digits of reversed digits
    sum = 0
    # loop through each digit
    for digit in reversed_digits:
        sum += digit
    # return the sum of digits in binary format
    return sum
