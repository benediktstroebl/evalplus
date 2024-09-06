
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
    # convert the number to a string
    # and append each letter in the string to a list
    digit_list = []
    N = str(N)
    for i in N:
        digit_list.append(i)
    # convert each number to an int and then 
    # add all the numbers to the sum
    sum = 0
    for i in digit_list:
        sum += int(i)
    # convert the sum to binary
    binary = bin(sum)
    return binary[2:]

