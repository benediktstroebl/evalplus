
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
    
    # convert the number to binary string
    binary = str(bin(N))
    # remove the 0b at the start of the string
    binary = binary[2:]
    # convert the string to list to be able to append items
    binary = list(binary)
    # count the total sum
    total_sum = 0
    # iterate through the digits in the binary number
    for digit in binary:
        # convert the digit from string to integer
        digit = int(digit)
        # add the digit to the total sum
        total_sum += digit
    # convert the total sum to binary
    total_sum = str(bin(total_sum))
    # remove the 0b at the start of the string
    total_sum = total_sum[2:]
    # return the total sum in binary
    return total_sum


