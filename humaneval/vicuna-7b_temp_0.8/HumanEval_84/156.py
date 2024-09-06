
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
    # check if the input number is negative
    if N < 0:
        return "-" + str(abs(N))[2:]
    
    # convert the input number to binary
    binary = str(N)
    
    # get the total number of digits in the binary representation
    num_digits = len(binary)
    
    # create an empty list to store the sum of digits
    sum_list = []
    
    # loop through all the digits in the binary representation
    for i in range(num_digits):
        # get the current digit and add it to the list
        digit = binary[i]
        sum_list.append(digit)
    
    # get the sum of all digits in the list
    sum = sum(sum_list)
    
    # convert the sum to binary and concatenate the result with the leading "1"
    binary_sum = str(sum)[2:]
    return "1" + binary_sum
