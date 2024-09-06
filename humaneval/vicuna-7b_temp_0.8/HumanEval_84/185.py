
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
    # Check if N is within range
    if N > 10000:
        return "10000"
    # Get the binary representation of N
    binary_repr = str(N)
    # Split the binary representation into a list of digits
    digits = binary_repr.split('')
    # Initialize a list to store the sum of digits
    digit_sum = [0] * (max(digits) + 1)
    # Loop over the digits and add them to the sum
    for i in range(len(digits)):
        digit_sum[digits[i]] += digit_sum[digits[i + 1]] if i < len(digits) - 1 else digit_sum[digits[i]]
    # Concatenate the digits of the sum
    result = ''.join([str(sum(x)) for x in digit_sum])
    return result
