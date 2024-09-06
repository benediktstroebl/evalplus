
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
    # Get the number of digits in binary
    num_digits = pow(2, N, 10)
    digits = []
    while num_digits:
        num_digits //= 2
        digits.append(num_digits % 10)

    # Combine the digits into a string
    binary_string = ''.join(map(str, digits))

    # Determine the length of the string
    len_string = len(binary_string)

    # Start at index 0 and iterate through the digits
    i = 0
    while i < len_string:
        # Determine the position of the rightmost digit
        rightmost_digit = i + len(binary_string) - 1

        # Check if the rightmost digit is 0
        if binary_string[rightmost_digit] == '0':
            rightmost_digit -= 1

        # If the rightmost digit is 0, add the current digit to the result
        if binary_string[rightmost_digit] == '1':
            result = result + '1'
            i += 1
        else:
            # If the rightmost digit is not 0, the result is 10^(log_2(N))
            result = '1' + '0' * (rightmost_digit - i - 1)
            i = rightmost_digit

    # Return the result
    return result
