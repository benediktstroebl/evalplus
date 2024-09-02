
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
    if N == 0:
        return "0"
    num_bits = N.bit_length()
    max_value = pow(2, num_bits - 1)
    min_value = pow(2, num_bits - 2)
    
    left_digit_sum = 0
    right_digit_sum = 0
    if N <= max_value:
        left_digit_sum = N - min_value
    else:
        left_digit_sum = 2 * (N - max_value) - 1
        
    right_digit_sum = left_digit_sum
    
    left_result = []
    while left_digit_sum != 0:
        left_digit = left_digit_sum % 2
        left_digit_sum = left_digit_sum // 2
        left_result.append(str(left_digit))
    
    right_result = []
    while right_digit_sum != 0:
        right_digit = right_digit_sum % 2
        right_digit_sum = right_digit_sum // 2
        right_result.append(str(right_digit))
    
    left_result.reverse()
    left_result = "".join(left_result)
    right_result = "".join(right_result)
    
    result = left_result + right_result
    
    return result
    
