
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
    # Create a dictionary to store the number in binary form with leading 1
    binary_map = {}
    for i in range(10):
        binary_map[i] = '1'

    # Create a list to store the digits of the input number
    digits = [str(N % i) for i in range(10)]

    # Create a list to store the number in binary form with leading 0
    binary_list = [0]

    # Loop through the digits of the input number
    for digit in digits:
        # Loop through the dictionary of binary numbers
        for digit_value in binary_map.values():
            # Add the current digit to the current binary number
            binary_list.append(str(digit_value) + digit)
        # Append a leading 0 to the current binary number
        binary_list.append('0' + ''.join(binary_list))

    # Return the number in binary form with leading 1
    return '1' + ''.join(binary_list)
