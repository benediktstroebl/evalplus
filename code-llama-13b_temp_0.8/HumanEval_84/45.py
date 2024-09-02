
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

    #find the binary number
    binary_num = bin(N).replace('0b', '')
    sum = 0
    #iterate through the binary number and add the value of each digit
    for i in range(0,len(binary_num)):
        sum += int(binary_num[i])
    #return the binary number of the final sum
    return bin(sum).replace('0b', '')


