
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
    # Define the value of N
    n = N
    # Iterate through each digit of the number
    while n != 0:
        # Append the current digit to the string
        digits.append(str(n % 10))
        # Divide the number by 10
        n = n // 10
    # Convert the string of digits to binary
    binary = ''.join(map(str, digits))
    # Convert the binary string to integer
    result = int(binary, 2)
    return result
