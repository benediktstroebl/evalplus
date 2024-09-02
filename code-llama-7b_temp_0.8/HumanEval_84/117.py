
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
    # Convert the input integer to a binary string
    binary_string = bin(N)
    # Split the string into a list of binary numbers
    binary_list = list(binary_string)
    # Reverse the list so the numbers are in the correct order
    binary_list.reverse()
    # Convert the list back to a string
    binary_string = ''.join(binary_list)
    # Split the string by the character 'b'
    binary_list = binary_string.split('b')
    # Remove the leading '0b'
    binary_list.pop(0)
    # Remove the trailing 'b'
    binary_list.pop(-1)
    # Return the sum of the numbers as a binary string
    return str(sum(map(int, binary_list)))
