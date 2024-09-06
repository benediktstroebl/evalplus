
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
    
    # If the number is greater than zero then proceed to find its binary sum
    if N > 0:
        # Convert the number to a binary number
        binary_N = bin(N)
        # Create an empty list to store the sum of binary numbers
        sum_bin = []
        # Split the binary number into a list of integers
        binary_N_list = list(binary_N[2:])
        # Loop through the list and find the sum of the binary numbers
        for i in binary_N_list:
            sum_bin.append(int(i))
        # Find the sum of the list
        sum_num = sum(sum_bin)
        # convert the sum back to binary
        sum_bin = bin(sum_num)
        # Remove the 0b at the front of the string
        sum_bin = sum_bin[2:]
        # return the sum in binary
        return str(sum_bin)
    # if the number is less than or equal to 0 then return 0
    else:
        return 0
        
