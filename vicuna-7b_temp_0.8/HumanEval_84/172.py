
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
    binary_representation = str(N)
    # convert binary_representation to list of digits
    digits = binary_representation.split(' ')
    # convert digits to list of integers
    int_digits = [int(x) for x in digits]
    # sum of digits
    sum = 0
    # iterate through the digits
    for num in int_digits:
        sum += num
    # convert sum to binary
    binary_sum = str(sum)
    # return the binary_sum
    return "1"*len(binary_sum) + binary_sum
